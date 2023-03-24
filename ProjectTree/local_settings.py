from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-0m5so0z&n2t5+##b%yc*7xo$f3&xkt^ompqn5xn7hhm7+zax@&'

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1",]



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}