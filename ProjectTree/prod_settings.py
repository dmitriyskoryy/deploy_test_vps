import os
from pathlib import Path
from .myconfig import *

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = SECRET_KEY


#  не забыть переключить в False !!!!!!!!!!!!
DEBUG = False

ALLOWED_HOSTS = ['92.255.79.72', 'localhost']



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
