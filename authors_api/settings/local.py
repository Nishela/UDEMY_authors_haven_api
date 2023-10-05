from .base import *  # noqa
from .base import env

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="BRYV5OIQAXkEfWrTMpMgTJ2tk6Z5_pvUBtAGlb0eq98pSitCo7w",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]
