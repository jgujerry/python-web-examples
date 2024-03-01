from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from src.config.settings import settings
from src.routes import router

__version__ = "0.0.1"


@asynccontextmanager
async def lifesapn(app: FastAPI):
    """fASTAPI application lifespan"""
    yield



app = FastAPI(
    title="FastAPI API",
    debug=settings.DEBUG,
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
