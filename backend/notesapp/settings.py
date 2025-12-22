from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'dummy-key'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'notesdb',
        'USER': 'notesuser',
        'PASSWORD': 'notespwd',
        'HOST': 'mysql',
        'PORT': '3306',
    }
}

ROOT_URLCONF = 'notesapp.urls'
MIDDLEWARE = []
