# Running the project

First of all you need to activate a virtual Python environment. All project
dependencies are stored in `requirements.txt` file. Just run

    $ virtualenv venv

to create the environment. Activate it using

    $ source venv/bin/activate

(your shell prompt should change a bit). Now install project dependencies with Pip

    (venv)$ pip install -r requirements.txt

## Local development

    $ ./manage.py runserver --settings horganizer.settings.local

be sure to have settings/local.py configuration file (you can copy the dist file
located in horganizer/settings). You can also run the project using uwsgi

    $ DJANGO_SETTINGS_MODULE=horganizer.settings.local uwsgi --http :8000 --module horganizer.wsgi
