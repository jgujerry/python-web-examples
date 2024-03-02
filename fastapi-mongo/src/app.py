from contextlib import asynccontextmanager

from beanie import init_beanie
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from motor.motor_asyncio import AsyncIOMotorClient

from src.config.settings import settings
from src.models import UserDocument, GroupDocument
from src.routes import router

__version__ = "0.0.1"


@asynccontextmanager
async def lifesapn(app: FastAPI):
    """fASTAPI application lifespan"""
    mongodb_uri = f"mongodb://{settings.MONGO_HOST}:{settings.MONGO_PORT}/{settings.MONGO_DB}"
    motor_client = AsyncIOMotorClient(mongodb_uri)
    
    await init_beanie(
        database=motor_client[settings.MONGO_DB],
        document_models=[
            GroupDocument,
            UserDocument
        ]
    )
    yield



app = FastAPI(
    title="FastAPI API",
    debug=settings.DEBUG,
    lifespan=lifesapn,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOW_ORIGINS,
    allow_methods=settings.ALLOW_METHODS,
    allow_headers=settings.ALLOW_HEADERS,
    allow_credentials=False,  # TODO: update based on requirement
)

app.include_router(router, prefix="/api")



@app.get("/")
async def welcome():
    return RedirectResponse("/api/")
