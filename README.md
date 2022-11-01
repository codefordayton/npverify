# NPVerify
Nonprofit verifier for Dayton Serves

NPVerify is a utility deployed to https://npverify.codefordayton.org/ to support folks checking for nonprofit websites.

NPVerify is a fairly simple [Django](https://www.djangoproject.com/) application. 

## Getting started

NPVerify is built on Django v4.1 and Python 3.10.

To get started:
* Download Python for your system. For the Mac, I use Homebrew to install it.

* Clone the repository.

* Set up a [virtual environment](https://pythonbasics.org/virtualenv/) in the directory.

* Set the following environment variables:
  * `export DEBUG=True`
  * `export DEVELOPMENT_MODE=True`

* Run `pip install -r requirements`.

* Run `python manage.py runserver` to start the debug server.

## Environment Variables

* `DJANGO_SECRET_KEY` - The secret key for the Django application. If none is defined, one will be generated.
* `DEBUG` - Enable/Disable Django debug mode. Having it enabled will cause Django to present stack traces to the user in the browser.
* `DEVELOPMENT_MODE` - Set to True to use a local sqlite3 database for the backend. If set to False, you will need to have a database url defined.
* `DATABASE_URL` - A database connection string following the format provided by [dj-database-url](https://pypi.org/project/dj-database-url/)
