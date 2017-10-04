from base import *


DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SITE_URL = 'https://coylec-streamthree-project.herokuapp.com'

PAYPAL_RECEIVER_EMAIL = config('PAYPAL_RECEIVER')
PAYPAL_TEST = True

RECAPTCHA_PUBLIC_KEY = config('CAP_PUB_KEY')
RECAPTCHA_PRIVATE_KEY = config('CAP_PRI_KEY')

NOCAPTCHA = config('NOCAPTCHA', cast=bool)

DISQUS_WEBSITE_SHORTNAME = config('DISQUS_NAME')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}