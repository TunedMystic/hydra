from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

from webapp import create_app
from webapp.extensions import db
from webapp.utils import find_db_models

app = create_app()
app_models = find_db_models()

def make_context():
  context = {x.__name__: x for x in app_models}
  context.update(**{
      "app": app,
      "db": db
  })
  return context

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command("db", MigrateCommand)
manager.add_command("shell", Shell(make_context=make_context))

if __name__ == "__main__":
    manager.run()
