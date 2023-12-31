from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-aj_(_@oan!gh^ht-p5-y@o5yyp)ubzm9n=&=#0)mk!$21=9=cy'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['agustinr87.pythonanywhere.com']

if not DEBUG: 
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
