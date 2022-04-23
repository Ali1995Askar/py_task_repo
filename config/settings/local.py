from .base import *

# CELERY SETTINGS
CELERY_BROKER_URL = env.str("CELERY_BROKER_URL", 'amqp://guest:guest@localhost:5672//')

# DataBase Settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.parent / 'db.sqlite3',
    }
}