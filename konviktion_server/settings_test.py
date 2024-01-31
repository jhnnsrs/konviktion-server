from .settings import *  # noqa
from .settings import DATABASES

DATABASES["default"] = {"ENGINE": "django.db.backends.sqlite3", "NAME": "db.sqlite3"}
