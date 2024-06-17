import os

def get_config(config_name):
    if config_name == 'development':
        from .development import DevelopmentConfig
        return DevelopmentConfig
    elif config_name == 'production':
        from .production import ProductionConfig
        return ProductionConfig
    else:
        from .base import BaseConfig
        return BaseConfig
