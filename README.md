# KTER Public API

Built with Django REST Framework
to serve data to the [React Client](https://github.com/joekennerly/kterclient)

## Index
---
0. [Getting Started](https://github.com/joekennerly/kterapi)
1. [Create Virtual Environment](https://github.com/joekennerly/kterapi)
---

## 0. Getting Started
To contribute to this project, you will need the following:
* Bash Terminal
* Python3
* Pip3
* Text Editor

## 1. Create virtual environment
Once you've cloned the repo, cd into it and run this command from your terminal:
```
python -m venv KterEnv
```
>Windows Users: this can be run in GitBash or Command Line

Start your virtual environment by running one of the following commands:
* Mac: `source ./KterEnv/bin/activate`
* Windows: `source ./KterEnv/Scripts/activate`

## 2. Install Dependencies
```
pip install -r requirements.txt
```

## 3. Initial Migrations
Now that the project is ready, we need to setup the database. Lucky for us, all of this is done by running a shell script:
```
./seed_db.sh
```
>Close **all** connections to the database if you need to reset the db

## 4. Start up the server
```
python manage.py runserver
```