
# Get started
## Dependencies
- Python 3.9
- Django 4.2

##  .venv
```bash
# create venv
python -m venv .venv

# activate
.venv/Scripts/Activate
```

## install django
```bash
python -m pip install Django==4.2

# check verison
python -m django --version
```

## Create Django project
```bash
django-admin startproject mysite

# run project
cd mysite
python manage.py runserver

# run with port
python manage.py runserver 0.0.0.0:8000

# migrate
python manage.py migrate
```

## create a app in project
https://docs.djangoproject.com/en/4.2/intro/tutorial01/#creating-the-polls-app
```bash
python manage.py startapp polls

# makemigrations when models change
#   must add PollsConfig to INSTALLED_APPS
python manage.py makemigrations polls

# view a polls migration sql step
python manage.py sqlmigrate polls 0001
python manage.py sqlmigrate polls 0002
```


## requirements file
```bash
# create file
pip freeze > requirements.txt

# install from requirement
pip install -r requirements.txt
```

## Documents
- https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html
- https://github.com/wsvincent/awesome-django