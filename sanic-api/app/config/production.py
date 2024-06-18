from .base import BaseConfig


class ProductionConfig(BaseConfig):
    DATABASE_URI = 'postgresql://user:password@localhost/prod_db'
    DEBUG = False
    PROXIES_COUNT = 3