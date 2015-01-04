"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import dj_database_url
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
if os.environ.get('DATABASE_URL'):
    DATABASES['default'] =  dj_database_url.config()



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6bpzesblxmghaycf(544_s56d@t7hujz3jz66ev4soi5z1masa'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'Users'),]

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "HTML"),
    os.path.join(BASE_DIR, "Graphs"),
    os.path.join(BASE_DIR, "HomePage"),
    os.path.join(BASE_DIR, "Dashboard"),
)

"""
Custom Added
"""

#AUTH_PROFILE_MODULE='accounts.UserProfile'
AUTH_USER_MODEL = 'userauth.Student'

#cookie based session
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

"""
End Custom
"""


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'userauth',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
