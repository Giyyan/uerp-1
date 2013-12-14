# coding=utf-8
import os
from os.path import basename

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SITE_NAME = basename(BASE_DIR)

ALLOWED_HOSTS = []

########## DEBUG CONFIGURATION
DEBUG = False

TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## MANAGER CONFIGURATION
ADMINS = (
    ('Giyyan', 'karbanovich.andrey@gmail.com'),
)

MANAGERS = ADMINS
########## END MANAGER CONFIGURATION


########## SECRET CONFIGURATION
SECRET_KEY = 'x*6ag5r8_ekmd85%xwj4ftrinex3ocuo+$o1l0&p132@r2j=xb'
########## END SECRET CONFIGURATION


########## END APP CONFIGURATION
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'south',
    'mptt',
    'django_mptt_admin',
)

LOCAL_APPS = (
    'uerp.apps.base',
    'uerp.apps.base.templatetags',

    'uerp.apps.res',
    'uerp.apps.ppc',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
########## END APP CONFIGURATION


########## MIDDLEWARE CONFIGURATION
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
########## END MIDDLEWARE CONFIGURATION


########## URL CONFIGURATION
ROOT_URLCONF = '%s.urls' % SITE_NAME
########## END URL CONFIGURATION

WSGI_APPLICATION = 'uerp.wsgi.application'


########## DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
    }
}
########## END DATABASE CONFIGURATION


########## GENERAL CONFIGURATION
LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True
########## END GENERAL CONFIGURATION


########## MEDIA CONFIGURATION
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
########## END STATIC FILE CONFIGURATION


########## TEMPLATE CONFIGURATION
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)
########## END TEMPLATE CONFIGURATION