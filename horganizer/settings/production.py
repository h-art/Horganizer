from .base import *

SECRET_KEY = 'YourSuperSecretKey'

####################
# turn off debugging
DEBUG = False
TEMPLATE_DEBUG = False

###############################
# mandatory if debugging is off
ALLOWED_HOSTS = ['*']
