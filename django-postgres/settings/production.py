from .common import *  # noqa: F403

DEBUG = False

ALLOWED_HOSTS = ["*"]

SECRET_KEY = env.str("DJANGO_SECRET_KEY")  # noqa: F405
