#!/usr/bin/env python
DEBUG = True
SECRET_KEY = 'super-ultra-secret-key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',

    'django_tables2',
    'django_tables2_column_shifter',
    'django_tables2_column_shifter.tests',
]

ROOT_URLCONF = 'django_tables2_column_shifter.tests.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

LANGUAGE_CODE = 'en-us'
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

MIDDLEWARE = []

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
