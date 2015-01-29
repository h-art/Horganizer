# Running the project

First of all you need to activate a virtual Python environment. All project
dependencies are stored in `requirements.txt` file. Just run

    $ virtualenv venv

to create the environment. Activate it using

    $ source venv/bin/activate

(your shell prompt should change a bit). Now install project dependencies with Pip

    (venv)$ pip install -r requirements.txt

## Local development

First of all, run migrations

    $ ./manage.py migrate --settings horganizer.settings.local

Then you will probably need to create a super user for the admin app

    ./manage.py createsuperuser --settings horganizer.settings.local

If you want to do this in just one command, simply run

    ./manage.py syncdb --settings horganizer.settings.local

At this point you can run Django's internal webserver to serve the application

    $ ./manage.py runserver --settings horganizer.settings.local

Be sure to have settings/local.py configuration file (you can copy the dist file
located in horganizer/settings). You can also run the project using uwsgi

    $ DJANGO_SETTINGS_MODULE=horganizer.settings.local uwsgi --http :8000 --module horganizer.wsgi
