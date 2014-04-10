"""
Django settings for mvp_landing project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(__file__)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+ig_rg5sdzs2^gp#3d1ee47#pr@dt3_wsl61^ex%)yeisjlo#!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catering',
    'sorl.thumbnail',
    'tagging',
    'photologue',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'foodspot.urls'

WSGI_APPLICATION = 'foodspot.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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

#Template location
TEMPLATE_DIRS =(
    os.path.join(os.path.dirname(BASE_DIR),'static', 'templates'),
)

if DEBUG:
    MEDIA_URL = '/media/'
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),'static', 'static-only') 
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),'static', 'media')
    STATICFILES_DIRS = (
        os.path.join(os.path.dirname(BASE_DIR),'static', 'static'),
    )

#Mail
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'secureYOUR-SERVER-NUMBER.hostgator.com'
#EMAIL_PORT = '26'
#EMAIL_HOST_USER = 'USER@YOURDOMAIN.COM'
#EMAIL_HOST_PASSWORD = 'THE-EMAIL-ACCOUNT-PASSWORD'
#EMAIL_USE_TLS = True
#To create a test SMTP server with Django just run this command via the python shell you had set up. It will not send the email buy as you run tests you will be able to see the content of your email display in the shell window.

  
#    python -m smtpd -n -c DebuggingServer localhost:102
