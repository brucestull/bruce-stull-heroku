# `bruce-stull` Porfolio Application Deployed on Heroku

## Heroku Application Links

* Application URL:
  * <https://bruce-stull.herokuapp.com/>

## Interesting Concepts, New and Old

### Will try out Railway for deployment, after copying the repository to another repository (`bruce-stull-railway`)

* [Django Tutorial Part 11: Deploying Django to production](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment)
  * <https://railway.app/dashboard>
* <https://docs.railway.app/getting-started>

### Django Tests

* Needed to add a `__init__.py` file to the 'tests' directories in order for the tests to run.

* Error:
  * `ImportError: 'tests' module incorrectly imported from 'C:\\Users\\FlynntKnapp\\Programming\\bruce-stull-heroku\\accounts\\tests'. Expected 'C:\\Users\\FlynntKnapp\\Programming\\bruce-stull-heroku\\accounts'. Is this module globally installed?`
    * Can only have either a `tests` directory or a `tests.py` file.
      * Initial directory structure:

        ```bash
        C:\USERS\FLYNNTKNAPP\PROGRAMMING\BRUCE-STULL-HEROKU\ACCOUNTS
        |   tests.py
        |
        \---tests
                test_models.py
                __init__.py
        ```

      * Final directory structure:

        ```bash
        C:\USERS\FLYNNTKNAPP\PROGRAMMING\BRUCE-STULL-HEROKU\ACCOUNTS
        |
        \---tests
                test_models.py
                __init__.py
        ```

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
