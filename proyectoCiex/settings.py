"""
Django settings for proyectoCiex project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_PATH = os.path.join(BASE_DIR,'templates')
STATIC_ROOT = 'staticfiles'
STATIC_PATH = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
MEDIA_URL = '/media/' 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

TEMPLATE_DIRS = (
    TEMPLATE_PATH,
)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


# Application definition
REGISTRATION_OPEN = True   #si esta en true los usuarios se pueden registrar a la aplicacion
ACCOUNT_ACTIVATION_DAYS = 7 #una semana para activacion de la cuenta
REGISTRATION_AUTO_LOGIN = True #si en true entonces el usuario despues de registrarse entra a la pagina
LOGIN_REDIRECT_URL = '/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(r47#dtma)lyi77k0$9s240y1etpc)uriob$t*xrk#)gq4xt8*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cafeteria',
    'registro',
    'comercializadora',
    'libreria',
    'libreria_puebla',
    'cafeteria_puebla',
    'control_puebla',
    'control'
)
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
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

ROOT_URLCONF = 'proyectoCiex.urls'

WSGI_APPLICATION = 'proyectoCiex.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database name',
        'USER':'db user',
        'PASSWORD': 'db pass',
        'HOST':'db host',
        'PORT':'3306'
    }
}
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


#import dj_database_url
#DATABASES['default'] = dj_database_url.config()

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

try:
    from .local_settings import *
except ImportError:
    pass