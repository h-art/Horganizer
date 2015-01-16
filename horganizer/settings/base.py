import os

#########################################################################
# this file contain base settings.
# ovverride base settings using environment-specific configuration files.
#########################################################################

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'av2+r=)sra-vy4-a^6wzpixa_f-a!omt7^uyo&j9^i6)^9$ie1'
DEBUG = True
TEMPLATE_DEBUG = True

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'horganizer.urls'
WSGI_APPLICATION = 'horganizer.wsgi.application'

LANGUAGE_CODE = 'it-it'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
MEDIA_ROOT = '/media/'
