# `bruce-stull` Porfolio Application

## Interesting Concepts

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
