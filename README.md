
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
```

## requirements file
```bash
# create file
pip freeze > requirements.txt

# install from requirement
pip install -r requirements.txt
```