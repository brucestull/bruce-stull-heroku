# Useful Commands and Links

## Development server web links

* Server Root:
  * <http://localhost:8000/>
* Projects:
  * <http://localhost:8000/projects/>
  * <http://localhost:8000/projects/1/>
  * <http://localhost:8000/projects/2/>
  * <http://localhost:8000/projects/3/>
* Blog:
  * <http://localhost:8000/blog/>
* Create user:
  * <http://localhost:8000/accounts/signup/>
* Django Admin:
  * <http://localhost:8000/admin/>
* Django Admin Documentation:
  * <http://localhost:8000/admin/doc/>
  * <http://localhost:8000/admin/doc/tags/>
  * <http://localhost:8000/admin/doc/filters/>
  * <http://localhost:8000/admin/doc/models/>
  * <http://localhost:8000/admin/doc/models/auth.user/>

## Production deployment links

* Dashboard:
* Server Root:
* Create user:
* Django Admin:
* Django Admin Documentation:

## Commands

### This Project

1. `pipenv install`
1. `pipenv shell`
1. `python manage.py migrate accounts`
1. `python manage.py migrate`
1. `python manage.py createsuperuser --email admin@email.app --username admin`
1. `python manage.py createsuperuser --email FlynntKnapp@email.app --username FlynntKnapp`
1. `python manage.py runserver`

### `pipenv`

* `pipenv install`
  * Create a `pipenv` virtual environment for the current directory.
* `pipenv install django==4.0`
* `pipenv install django==4.1`
* `pipenv install docutils==0.19`
* `pipenv install social-auth-app-django`
* `pipenv shell`
* `exit`
  * Exit the current `pipenv` virtual environment.

### `pip`

* `pip list`

### Django

* `django-admin startproject the_project .`
* `python manage.py startapp the_app`
* `python manage.py runserver`
* `<Ctrl+C>`
* `python manage.py makemigrations`
* `python manage.py migrate`
* `python manage.py createsuperuser`
* `python manage.py createsuperuser --email admin@email.app --username admin`

### Django Create `SECRET_KEY`

* `python manage.py shell`
* `from django.core.management.utils import get_random_secret_key`
* `print(get_random_secret_key())`

### Heroku

* Can't have leading `.\` when running command with `heroku run`:
  * `heroku run python manage.py createsuperuser --email admin@email.app --username admin`
  * `heroku run python manage.py createsuperuser --email FlynntKnapp@email.app --username FlynntKnapp`
* `heroku login`
* `heroku create dezzi-diner`

### PowerShell

* `Get-Command python | Format-List *`

### Misc

* `tree /f /a`

### Git

* `git remote -v`

## Repository Links

* Repository [`README.md`](../README.md).
