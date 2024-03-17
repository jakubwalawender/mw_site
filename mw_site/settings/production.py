from .base import *

DEBUG = False
ALLOWED_HOSTS = ['szpuk.pythonanywhere.com']
ROOT_URLCONF = 'mw_site.urls'

SECRET_KEY = os.getenv("SECRET_KEY")

try:
    from .local import *
except ImportError:
    pass
