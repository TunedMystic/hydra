from __future__ import absolute_import

from importlib import import_module
from flask import blueprints

from webapp import settings
from webapp.extensions import db


class ObjectFinder(object):
    """
    A Class responsible for searching through modules
    to find classes that meet a specific criteria.
    Used to dynamically load any type of class.
    """

    check_functions = {
        "instance": lambda obj, kls, mod_name: isinstance(obj, kls),
        "subclass": lambda obj, kls, mod_name:
            issubclass(obj, kls) and obj.__module__ == mod_name
    }

    # Exclude these keys in a module's __dict__.
    exclude_keys = (
        "__builtins__",
        "__file__",
        "__package__",
        "__name__",
        "__doc__"
    )

    def __init__(self, **kwargs):
        self.installed_apps = kwargs.pop("installed_apps")
        self.project_name = kwargs.pop("project_name")
        self.submodule_name = kwargs.pop("submodule_name")
        self.klass = kwargs.pop("klass")
        self.check_type = kwargs.pop("check_type")

    def iterate_apps(self, submodule_name=None):
        """
        Iterate through all Flask apps, and
        return an absolute module name.
        """
        for flask_app in self.installed_apps:
            module_path = self.project_name + "." + flask_app
            if submodule_name:
                module_path += "." + submodule_name
            yield module_path

    def get_check_method(self, check_method_name):
        """
        Return the function fo filter objects in the module.
        """
        method = self.check_functions.get(check_method_name)
        if not method:
            raise Exception(
                "Check method {0} is not supported."
                .format(check_method_name)
            )
        return method

    def find_all_objects(self):
        """
        Iterate through all apps in the Flask application, and
        return all instances that either inherit from, or is
        an instance of a certain class.

        submodule_name: The python module path to search in.
        klass:          The class to search for subclasses of.
        check_type:     The function to filter objects in a module.
        """
        instances = []
        check_method = self.get_check_method(self.check_type)
        for module_name in self.iterate_apps(self.submodule_name):
            try:
                # Import the models module
                module = import_module(module_name)
                # Iterate through module's __dict__.
                for name in module.__dict__.keys():
                    # Exclude the listed keys.
                    if name not in self.exclude_keys:
                        try:
                            value = module.__dict__[name]
                            if check_method(value, self.klass, module_name):
                                instances.append(value)
                        except:
                            pass
            except:
                raise Exception("No module named {0}".format(module_name))
        return instances


def find_db_models():
    """
    Search through the Flask application and return a list
    of all models that subclass from <SQLAlchemy.Model>.
    """
    finder_kwargs = {
        "installed_apps": settings.INSTALLED_APPS,
        "project_name": settings.PROJECT_NAME,
        "submodule_name": "models",
        "klass": db.Model,
        "check_type": "subclass"
    }
    finder = ObjectFinder(**finder_kwargs)
    return finder.find_all_objects()


def find_blueprints():
    """
    Search through the Flask application and return a list
    of all <flask.blueprints.Blueprint> instances.
    """
    finder_kwargs = {
        "installed_apps": settings.INSTALLED_APPS,
        "project_name": settings.PROJECT_NAME,
        "submodule_name": "views",
        "klass": blueprints.Blueprint,
        "check_type": "instance"
    }
    finder = ObjectFinder(**finder_kwargs)
    return finder.find_all_objects()


if __name__ == '__main__':
    m = find_db_models()
    #m = find_blueprints()
    print m
