import os

INSTALLED_APPS = (
    "base",
    "wire",
)

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

PROJECT_NAME = os.path.basename(PROJECT_DIR)

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(PROJECT_DIR, "db.sqlite3")

WTF_CSRF_ENABLED = True

SECRET_KEY = "insert-cool-secret-key-here"
