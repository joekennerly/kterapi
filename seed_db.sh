#!/bin/bash

rm -rf kterapi/migrations
rm db.sqlite3
python manage.py makemigrations kterapi
python manage.py migrate
python manage.py loaddata vendor
python manage.py loaddata customer
python manage.py loaddata token
python manage.py loaddata productcategory
python manage.py loaddata product
python manage.py loaddata favorite
python manage.py loaddata payment
python manage.py loaddata order
python manage.py loaddata orderproduct