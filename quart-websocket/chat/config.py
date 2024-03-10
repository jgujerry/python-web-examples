import os

__all__ = ["AppConfig"]


class ConfigBase:
    DEBUG = False
    SECRET_KEY = "quart"


class DevelopmentConfig(ConfigBase):
    DEBUG = True


class ProductionConfig(ConfigBase):
    SECRET_KEY = os.environ.get("QUART_SECRET_KEY")


def get_config(env):
    """Return configuration based on environment"""
    if env == "production":
        return ProductionConfig

    return DevelopmentConfig


env = os.getenv("QUART_ENV", "development")
AppConfig = get_config(env)
