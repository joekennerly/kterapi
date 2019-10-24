#!/bin/bash

rm -rf kterapi/migrations
rm db.sqlite3
python manage.py makemigrations kterapi
python manage.py migrate
python manage.py loaddata vendor