from base import *


DEBUG = True

INSTALLED_APPS.append('debug_toolbar')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SITE_URL = 'http://127.0.0.1:8000'
PAYPAL_RECEIVER_EMAIL = config('PAYPAL_RECEIVER')
PAYPAL_TEST = True

RECAPTCHA_PUBLIC_KEY = config('CAP_PUB_KEY')
RECAPTCHA_PRIVATE_KEY = config('CAP_PRI_KEY')

NOCAPTCHA = config('NOCAPTCHA', cast=bool)

DISQUS_WEBSITE_SHORTNAME = config('DISQUS_NAME')

MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')