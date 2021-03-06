"""
Django settings for iot_site project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x%5vairsj-)6yl(3%mw4h35a3=kz)u^m@4v^z+qnod!pa((p*&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'iot_site.apps.iot_api',
    'iot_site.apps.iot_app',
    'iot_site.apps.iot_accounts',
    'iot_site.apps.iot_charts',
    'iot_site.apps.iot_query',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'bootstrap4',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'iot_site.middleware.LoginRequiredMiddleware',
]

ROOT_URLCONF = 'iot_site.urls'

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

WSGI_APPLICATION = 'iot_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite3'),
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'


# Built-in User Model

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda x: '/accounts/profile',
}

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


# bootstrap4 settings

BOOTSTRAP4 = {
    'javascript_in_head': True,
}


# LoginRequiredMiddleware

LOGIN_REQUIRED_EXEMPT_URLS = [
    '^$',
    '^admin/.*',
    '^accounts/.*',
    '^api/api-auth/.*',
]


# InfluxDB

INFLUXDB = {
    'HOST': os.environ.get('INFLUXDB_SERVICE_HOST', 'influxdb'),
    'PORT': os.environ.get('INFLUXDB_SERVICE_PORT', 8086),
    'USER': os.environ.get('INFLUXDB_USER', None),
    'PASSWORD': os.environ.get('INFLUXDB_PASSWORD', None),
    'DATABASE': os.environ.get('INFLUXDB_DATABASE', 'iot_metrics'),
}
