rm db.sqlite3
rm -rf migrations/
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
