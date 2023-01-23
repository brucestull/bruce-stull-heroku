# Notes

## Interesting Concepts

### Django Tests

* Needed to add a `__init__.py` file to the 'tests' directories in order for the tests to run.
* Django test snippets:
  * Run all tests in all apps.
    * `python manage.py test`

### Production Deployment

* `SECRET_KEY`:

  ```python
  import os

  SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag'
  )
  ```

* `DEBUG`:

  ```python
  import os

  DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'
  ```

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
  * `config`
    * Django project configuration
  * `blog`
    * Blog application
  * `projects`
    * Projects application
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

## Creating a Couple `Project` Objects

1. Start Django admin shell:

    * `python manage.py shell`

1. Create `Project` objects:

```python
from projects.models import Project
from accounts.models import CustomUser

the_owner = CustomUser.objects.get(pk=1)

p1 = Project(
title="First Project",
description="Just an image???",
owner=the_owner,
image="images/test_image_01.png",
)

p1.save()

p2 = Project(
title="Second Project",
description="Just an image???",
owner=the_owner,
image="images/test_image_02.png",
)

p2.save()

p3 = Project(
title="Third Project",
description="Just an image???",
owner=the_owner,
image="images/test_image_03.png",
)

p3.save()
```

## `realpython.com` Image Location

* `C:\Users\FlynntKnapp\Programming\realpython\rp-portfolio\projects\static\img\project1.png`
* `rp-portfolio\projects\static\img\project2.png`

## Resources

* <https://rorydeken.github.io/Buckeye-Ipsum/>
