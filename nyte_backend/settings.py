"""
Django settings for nyte_backend project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import django_heroku
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!7w4cqjl!s)a$kx@vsy4%wy8q9ii1y9lbf8^@#gprb_+k7kapn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api.apps.ApiConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'drf_extra_fields',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nyte_backend.urls'

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

WSGI_APPLICATION = 'nyte_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nyte',
        'USER': 'zach',
        'PASSWORD': 'HelloEd12',
        'HOST': 'localhost',
        'PORT': '5432',
        'TEST': {
            'NAME': 'd441dv4c85a2q3',
        },
    }
}

import dj_database_url
DATABASES['default'] = dj_database_url.config(default='postgres://zach:HelloEd12@localhost:5432/nyte', conn_max_age=600)


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = 'static/'
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static/')

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media/")

AUTH_USER_MODEL = 'api.NyteUser'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        #'rest_framework.authentication.TokenAuthentication',
        #"api.authentication.NyteAuthentication",
    ],

    'DEFAULT_PERMISSION_CLASSES': [
        #'rest_framework.permissions.IsAuthenticated',
    ]
}

#facebook auth settings
#FACEBOOK_APP_ID = '2319283855026340' #personal account kit testing
FACEBOOK_APP_ID = '2135369323179432' #kyles account kit testing
#FACEBOOK_APP_SECRET = '0d09b9bac681e1634e31f6c4b8f68a24' #personal account kit testing
FACEBOOK_APP_SECRET = '5ec3d6f70405ddde44602e959627e19c' #kyles account kit testing

#twilio auth settings
TWILIO_ACCOUNT_SID = "AC422f24dc82bfa93152575ddb69d1d2ec"
TWILIO_AUTH_TOKEN = "9852d9a25123abcc7aa73998b033807c"
TWILIO_FROM_NUM = ""

#Age checker settings
AGE_CHECKER_API_KEY = "xmTU0wA12zFhg2mZmiQ0ookNoSUZ68S4"
AGE_CHECKER_SECRET = "yqKqNATKU00yA1ie"

#strip settings
STRIPE_PUBLIC_KEY = "pk_test_ut867fONoVm163Ro4J1QX5sh00XREjDW6f"
STRIPE_SECRET_KEY = "sk_test_DjOGG9xXc9hKkm15WpoNOntz00LBttlsdL"

django_heroku.settings(locals())