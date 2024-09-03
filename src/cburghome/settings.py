"""
Django settings for cburghome project.

Generated by 'django-admin startproject' using Django 5.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
from decouple import config
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# print('BASE_DIR: ', BASE_DIR)

# default backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# email config
EMAIL_HOST = config("EMAIL_HOST", cast=str, default=None)
EMAIL_PORT = config("EMAIL_PORT", cast=str, default='587') # Recommended
EMAIL_HOST_USER = config("EMAIL_HOST_USER", cast=str, default=None)
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", cast=str, default=None)
EMAIL_USE_TLS = config("EMAIL_USE_TLS", cast=bool, default=True)  # Use EMAIL_PORT 587 for TLS
EMAIL_USE_SSL = config("EMAIL_USE_SSL", cast=bool, default=False)  # Use MAIL_PORT 465 for SSL

ADMIN_USER_NAME=config("ADMIN_USER_NAME", default="Admin user")
ADMIN_USER_EMAIL=config("ADMIN_USER_EMAIL", default=None)

# 500(Internal Server Error) errors are emailed to these users
MANAGERS=[]
ADMINS=[]
if all([ADMIN_USER_NAME, ADMIN_USER_EMAIL]):    
    ADMINS +=[
        (f"{ADMIN_USER_NAME}", f"{ADMIN_USER_EMAIL}")
    ]
    MANAGERS=ADMINS


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("DJANGO_SECRET_KEY", default=None)
# print("SECRET_KEY: ", SECRET_KEY)

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
# DEBUG= str(os.environ.get("DJANGO_DEBUG")).lower()=="true"
DEBUG=config("DJANGO_DEBUG", default=False, cast=bool)
# print("DEBUG: ", DEBUG, type(DEBUG))

BASE_URL=config("BASE_URL", default=None, cast=str)

# until now local host is run. to deploy it, change allowed_hosts
ALLOWED_HOSTS = [
    "saas-django-tut.onrender.com"
]

if DEBUG:
    ALLOWED_HOSTS+=[
        "127.0.0.1",
        "localhost"
    ]


# Application definition

INSTALLED_APPS = [
    # django-apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # plural names
    # my-apps
    'visits',
    'profiles',
    'dashboard',
    'subscriptions',
    'customers',    
    'commando',        
    #third-party apps
    'allauth_ui',
    'allauth',
    'allauth.account',        
    'allauth.socialaccount', 
    'allauth.socialaccount.providers.github',
    'widget_tweaks',
    'slippers'
]

# ?: (slippers.E001) Slippers was unable to find a components.yaml file.
#         HINT: Make sure it's in a root template directory.
# refer  https://mitchel.me/slippers/docs/registering-components/

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #  Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cburghome.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/ "templates"],
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

WSGI_APPLICATION = 'cburghome.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# not ready for production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASE_URL=config("DATABASE_URL", cast=str)
DATABASE_URL=config("DATABASE_URL", default=None)
CONN_MAX_AGE= config("CONN_MAX_AGE", cast=int, default=30)


if DATABASE_URL is not None:
    import dj_database_url
    # Returns configured DATABASE dictionary from DATABASE_URL.
    DATABASES = {
        'default': dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age= CONN_MAX_AGE,
            conn_health_checks=True
            )        
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

# django all-auth-ui config
# light, winter, retro, business, corporate --good ones
ALLAUTH_UI_THEME = "corporate"

# django all-auth config
LOGIN_REDIRECT_URL='/'
ACCOUNT_AUTHENTICATION_METHOD="username_email"
ACCOUNT_EMAIL_VERIFICATION="mandatory"
ACCOUNT_EMAIL_SUBJECT_PREFIX=" [SaaS] "
ACCOUNT_EMAIL_REQUIRED=True
AUTHENTICATION_BACKENDS = [    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend'
]

# Provider specific settings
# social authentication
SOCIALACCOUNT_PROVIDERS = {
    'github': {        
        "VERIFIED_EMAIL": True
    }
}


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_BASE_DIR= BASE_DIR/ "staticfiles"
STATICFILES_BASE_DIR.mkdir(exist_ok=True, parents=True)
STATICFILES_VENDOR_DIR= STATICFILES_BASE_DIR/ "vendors"

# source(s) for python manage.py collectstatic
STATICFILES_DIRS=[
    STATICFILES_BASE_DIR
]

# output for for python manage.py collectstatic
# local-cdn -> prod-cdn
STATIC_ROOT= BASE_DIR/ "local-cdn"

# < DJANGO 4.2
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# > DJANGO 4.2 >
STORAGES = {    
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
