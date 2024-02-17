import os


class Config:
    DEBUG = False
    SECRET_KEY = "quart"


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    SECRET_KEY = os.environ.get("QUART_SECRET_KEY")


def get_config(env):
    """Return configuration based on environment"""
    if env == "production":
        return ProductionConfig
    
    return DevelopmentConfig
