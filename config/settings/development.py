from config.settings.common import *
import os


DEBUG = True


ALLOWED_HOSTS = ['localhost']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# Create your own `DJANGO_SECRET_KEY` here for use in Development.
# This one is provided here for user to get the DjangoCustomUserStarter up and running quickly.
    # Ideally, you would not run with `DJANGO_SECRET_KEY` exposed in development either.
        # You can set a `DJANGO_SECRET_KEY` on you development computer system.
        # Create a specific `DJANGO_SECRET_KEY` for development and use it in development only.
        # Create a specific `DJANGO_SECRET_KEY` for production and use it in production only.

SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    '4dm7#s0rwxnkhqk&c9*-==xkrreet1+8n)u^-yapdilj7ppzw0',
)

# To create a new `DJANGO_SECRET_KEY`:
"""
    python .\manage.py shell
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())
"""
