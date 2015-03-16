from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

from webapp import create_app
from webapp.extensions import db
from webapp.utils import find_db_models

app = create_app()
app_models = find_db_models()

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command("db", MigrateCommand)
manager.add_command("shell", Shell())

if __name__ == "__main__":
    manager.run()
