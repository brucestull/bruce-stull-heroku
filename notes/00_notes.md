# Notes

## Current Location in Documentation

* <https://realpython.com/django-view-authorization/>

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

## RealPython - MyApp Viewname Mappings

* `dashboard` - `projects:index`

## Password Reset Notes

* We already have another method to reset passwords, so we'll just use that one for now.
  * <https://realpython.com/django-user-management/#send-password-reset-links>
  * `python -m smtpd -n -c DebuggingServer localhost:1025`
* <https://realpython.com/django-user-management/#change-email-templates>

### Send Password Reset Links to Real Email Addresses

* <https://realpython.com/django-user-management/#send-emails-to-the-outside-world>

* Environment Variables
  * `SMTP_HOSTNAME`
  * `SMTP_PORT`
  * `SMTP_USERNAME`
  * `SMTP_PASSWORD`

## GitHub OAuth Notes

* Create the GitHub OAuth application
  * <https://github.com/settings/applications/new>
    INSERT_IMAGE_HERE

* `https://github.com/login/oauth/authorize?client_id=None&redirect_uri=http://localhost:8000/accounts/oauth/complete/github/&state=lrgKWJgVwjBpvyfcNAEuZrnVYFGIVnHm&response_type=code`

## Directory Structure

  ```bash
  C:\USERS\FLYNNTKNAPP\PROGRAMMING\BRUCE-STULL
  |   .gitignore
  |   db.sqlite3
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
              profile_update.html
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
* <https://github.com/python-social-auth/social-app-django>
  * <https://python-social-auth.readthedocs.io/en/latest/configuration/django.html>
