# https://sanic.dev/en/guide/running/configuration.html

class BaseConfig:
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'
    OAS_URL_PREFIX = '/docs'

