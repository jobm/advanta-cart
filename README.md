# Advanta Cart

#### Local Project Set-Up
   1. Create a virtual environment 
   2. `pip install -r requirements.txt` into the venv
   3. create `local_setting.py` and import it in `settings.py`
   4. Add your local setting to `local_settings.py` e.g. db, email e.t.c

#### Using Postgres Locally
- To use postgres make sure you create a database using psql then have the following settings in your `local_settings.py` file.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbname',
        'USER': 'user',
        'PASSWORD': password,
        'HOST': host,
        'PORT': '5432',
    }
}
```
Once the setup is done:
1. Run `./manage.py makeigrations` then `./manage.py migrate`.
2. Run `./manage.py createsuperuser` and follow steps to create the admin.
3. Finally run `./manage.py runserver` and visit localhost:8000 on your browser.

### Tools used
1. Python 2.7, Django 1.11.2 (Backend) 
2. HTML, CSS JS and MDBootstrap for (UI)
3. Heroku for Deployment.

