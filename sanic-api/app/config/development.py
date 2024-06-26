from .base import BaseConfig


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    DATABASE_URI = 'sqlite:///dev_db.sqlite3'
    PROXIES_COUNT = 1

