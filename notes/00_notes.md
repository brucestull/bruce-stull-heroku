# Notes

## Tutorial Links

* [Get Started With Django Part 1: Build a Portfolio App](https://realpython.com/get-started-with-django-1/)
* [Get Started With Django Part 2: Django User Management](https://realpython.com/django-user-management/)
* [Get Started With Django Part 3: Django View Authorization](https://realpython.com/django-view-authorization/)

## Heroku Application Links

* Git Repository:
  * <https://git.heroku.com/bruce-stull.git>
* Application URL:
  * <https://bruce-stull.herokuapp.com/>

## Planned Directory Structure

* `bruce-stull`
  * `accounts`
    * User account management
  * `blog`
    * Blog application
  * `config`
    * Django project configuration
  * `portfolio`
    * Portfolio application
  * `templates`
    * Django templates from DjangoCustomUserStarter

## Directory Structure

  ```bash
  C:\USERS\FLYNNTKNAPP\PROGRAMMING\BRUCE-STULL
  |   .gitignore
  |   db.sqlite3
  |   LICENSE
  |   manage.py
  |   Pipfile
  |   Pipfile.lock
  |   Procfile
  |   README.md
  |
  +---.vscode
  |       launch.json
  |
  +---accounts
  |   |   admin.py
  |   |   apps.py
  |   |   forms.py
  |   |   models.py
  |   |   tests.py
  |   |   urls.py
  |   |   views.py
  |   |   __init__.py
  |   |
  |   \---migrations
  |       |   0001_initial.py
  |       |   __init__.py
  |       |
  |       \---__pycache__
  |               0001_initial.cpython-311.pyc
  |               __init__.cpython-311.pyc
  |
  +---config
  |   |   asgi.py
  |   |   urls.py
  |   |   wsgi.py
  |   |   __init__.py
  |   |
  |   \---settings
  |       |   common.py
  |       |   development.py
  |       |   production.py
  |       |
  |       \---__pycache__
  |               common.cpython-311.pyc
  |               development.cpython-311.pyc
  |
  +---notes
  |       00_commands_and_links.md
  |       00_directory_structure.md
  |       00_notes.md
  |
  \---templates
      |   base.html
      |   home.html
      |   staff.html
      |   user.html
      |
      \---registration
              login.html
              password_reset_complete.html
              password_reset_confirm.html
              password_reset_done.html
              password_reset_form.html
              signup.html
              update.html
  ```
