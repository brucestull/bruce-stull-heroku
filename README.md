# `bruce-stull` Porfolio Application Deployed on Heroku

## Heroku Application Links

* Application URL:
  * <https://bruce-stull.herokuapp.com/>

## Interesting Concepts

### Will try out Railway for deployment, after copying the repository to another repository (`bruce-stull-railway`)

* [Django Tutorial Part 11: Deploying Django to production](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment)
  * <https://railway.app/dashboard>
* <https://docs.railway.app/getting-started>

### Django Tests

* Needed to add a `__init__.py` file to the 'tests' directories in order for the tests to run.

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
