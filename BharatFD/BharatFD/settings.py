"""
Django settings for BharatFD project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i5y5n&bx+j45o9tqk_1wo^c0t!&)k8lu70g^&5qcf007$50745'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     'ckeditor',
    'ckeditor_uploader', 
     'faq',
     'rest_framework'
]

# CKEditor Configuration
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
        'language': 'en',  # Default language
        'toolbar_full': [
            ['Format', 'Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker'],
            ['NumberedList', 'BulletedList', 'Indent', 'Outdent', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink', 'Anchor'],
            ['Table', 'HorizontalRule', 'SpecialChar'],
            ['Source'],
            ['Maximize'],
        ],
        'extraPlugins': ','.join([
            'autogrow',
            'language',
            'specialchar',
            'clipboard',
            'notification',
        ]),
    },
    # Add the 'hindi' configuration here
    'hindi': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
        'language': 'hi',  # Hindi language
        'font_names': 'Arial;Times New Roman;Noto Sans Devanagari',
        'contentsLangDirection': 'rtl',  # Set text direction to right-to-left for Hindi
        'extraPlugins': ','.join([
            'autogrow',
            'language',
            'specialchar',
            'emoji',  # Add more plugins if needed
        ]),
    },
    'bengali': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
        'language': 'bn',  # Bengali language
        'font_names': 'Arial;Times New Roman;Noto Sans Bengali',  # Use appropriate font for Bengali
        'contentsLangDirection': 'ltr',  # Set text direction to left-to-right for Bengali
        'extraPlugins': ','.join([
            'autogrow',
            'language',
            'specialchar',
            'emoji',
        ]),
    },
    'gujarati': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
        'language': 'bn',  # Bengali language
        'font_names': 'Arial;Times New Roman;Noto Sans Bengali',  # Use appropriate font for Bengali
        'contentsLangDirection': 'ltr',  # Set text direction to left-to-right for Bengali
        'extraPlugins': ','.join([
            'autogrow',
            'language',
            'specialchar',
            'emoji',
        ]),
    },
    'telugu': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
        'language': 'bn',  # Bengali language
        'font_names': 'Arial;Times New Roman;Noto Sans Bengali',  # Use appropriate font for Bengali
        'contentsLangDirection': 'ltr',  # Set text direction to left-to-right for Bengali
        'extraPlugins': ','.join([
            'autogrow',
            'language',
            'specialchar',
            'emoji',
        ]),
    },
    'tamil': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
        'language': 'ta',  # Tamil language
        'font_names': 'Arial;Times New Roman;Noto Sans Tamil',  # Use appropriate font for Tamil
        'contentsLangDirection': 'ltr',  # Set text direction to left-to-right for Tamil
        'extraPlugins': ','.join([
            'autogrow',
            'language',
            'specialchar',
            'emoji',
        ]),
    },
    'telgu': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
        'language': 'ta',  # Tamil language
        'font_names': 'Arial;Times New Roman;Noto Sans Tamil',  # Use appropriate font for Tamil
        'contentsLangDirection': 'ltr',  # Set text direction to left-to-right for Tamil
        'extraPlugins': ','.join([
            'autogrow',
            'language',
            'specialchar',
            'emoji',
        ]),
    },
    'kannada': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
        'language': 'ta',  # Tamil language
        'font_names': 'Arial;Times New Roman;Noto Sans Tamil',  # Use appropriate font for Tamil
        'contentsLangDirection': 'ltr',  # Set text direction to left-to-right for Tamil
        'extraPlugins': ','.join([
            'autogrow',
            'language',
            'specialchar',
            'emoji',
        ]),
    },
}





# File upload settings (if needed)
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js'

#radis implementation
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',  # Redis instance
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'BharatFD.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
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

WSGI_APPLICATION = 'BharatFD.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",  # This is the directory where your static files will live
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
