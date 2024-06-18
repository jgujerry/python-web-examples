from .development import DevelopmentConfig
from .production import ProductionConfig


def get_config(env):
    if env == 'production':
        return ProductionConfig
    else:
        return DevelopmentConfig
