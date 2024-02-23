import os

__all__ = ["AppConfig"]


class ConfigBase:
    """Base configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    

class DevelopmentConfig(ConfigBase):
    """Development configuration"""
    APP_ENV = "development"
    DEBUG = True


class TestingConfig(ConfigBase):
    """Testing configuration"""
    APP_ENV = "testing"
    DEBUG = False
    TESTING = True


class ProductionConfig(ConfigBase):
    """Production configuration"""
    APP_ENV = "production"
    DEBUG = False


def get_config(env):
    if env == "production":
        return ProductionConfig
    elif env == "testing":
        return TestingConfig
    else:
        return DevelopmentConfig


env = os.getenv("FLASK_ENV", "development")
AppConfig = get_config(env)
