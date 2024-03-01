import os


from pydantic_settings import BaseSettings

__all__ = ["AppConfig"]


class CommonSettings(BaseSettings):
    # ENVIRONMENT
    FASTAPI_ENV: str
    
    # fASTAPI
    DEBUG: str = False
    SECRET_KEY: str = "fastapi"
    
    # CORS
    ALLOW_ORIGINS: list[str] = ["*"]
    ALLOW_METHODS: list[str] = ["*"]
    ALLOW_HEADERS: list[str] = ["*"]
    
    # MONGO
    MONGO_HOST: str
    MONGO_PORT: str
    MONGO_DB: str


class DevelopmentSettings(CommonSettings):
    FASTAPI_ENV: str = "development"
    DEBUG: bool = True


class ProductionSettings(CommonSettings):
    FASTAPI_ENV: str = "production"
    SECRET_KEY: str = os.environ.get("FASTAPI_SECRET_KEY")


def get_settings(env):
    """Return configuration based on environment"""
    if env == "production":
        return ProductionSettings()

    if env == "development":
        return DevelopmentSettings()

    raise ValueError(f"Not a valid environment, please use 'development' or 'production'")


env = os.getenv("FASTAPI_ENV", "development")
settings = get_settings(env)
