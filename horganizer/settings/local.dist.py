from .base import *

############################################
# load staticfiles app for local development
INSTALLED_APPS = INSTALLED_APPS + ('django.contrib.staticfiles',)

###################
# database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
