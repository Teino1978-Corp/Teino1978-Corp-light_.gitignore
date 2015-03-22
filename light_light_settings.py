import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from django.core.urlresolvers import reverse_lazy

LOGIN_URL = reverse_lazy('login')
LOGIN_REDIRECT_URL = reverse_lazy('timeline')
LOGOUT_URL = reverse_lazy('logout')

SECRET_KEY = '_f=fga5pp@z#0^k*94^c&@#&cs+_b!h*s^0-m71*u(-d!-tx5!'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'authenticated',
    'indicators',
    'data',
    'master',
    'financials',
    'imports',
    'reports',
    'random_messages',
    'design',
    'actions',
    'test_db',
    'temp',
    'chat',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "design.context_processors.menu",
    "design.context_processors.chat",
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'light.urls'

WSGI_APPLICATION = 'light.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'xe',
        'USER': 'light',
        'PASSWORD': 'gestionventas',
        'HOST': 'localhost',
        'PORT': '1521'
    }
}

LANGUAGE_CODE = 'es-CL'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static', 'static'),
)

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')
MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, 'design', 'templates'),
    os.path.join(BASE_DIR, 'actions', 'templates'),
)

SESSION_EXPIRE_AT_BROWSER_CLOSE = True