import os


class AppConfig:
    """Base configuration"""
    TESTING = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    

class DevelopmentConfig(AppConfig):
    """Development configuration"""
    DEBUG = True
    DEVELOPMENT = True


class TestingConfig(AppConfig):
    """Testing configuration"""
    TESTING = True


class ProductionConfig(AppConfig):
    """Production configuration"""
    DEBUG = False
