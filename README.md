# API Transparência Unicamp 

## Install

### Requirements

We use [Django](http://djangoproject.com) in the backend. That said the basic requirement is [Python](http://python.org) 3.5 with `pip` ([virtualenv](http://virtualenv.readthedocs.org) recommended).

### Dependencies

Once you have `pip` available let's install the dependencies:

```
pip install -r requirements.txt
```

### Settings

Copy `contrib/.env.sample` as `.env` in the project's root folder and adjust your settings.

At this point it's crucial to configure the acceess to you database ([PostgreSQL](http://www.postgresql.org) is not required, but recommended).

### Migrations

Once you're done with requirements, dependencies and settings, create the basic structure at the database and create a super-user for you:

```
python manage.py migrate
python manage.py createsuperuser
```

### Ready?

Not sure? Run `python manage.py check` and `python manage.py test` just in case.

### Accessing the API

Run the server with `python manage.py runserver` and load [localhost:8000](http://localhost:8000) with your favorite browser.

If you want to test the _login required_ area, as a developer you can login through [Django Admin](http://localhost:8000/admin/) and then go back to the [root](http://localhost:8000/).