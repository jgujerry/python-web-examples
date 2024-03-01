import logging

from fastapi import APIRouter

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/")
async def hello():
    logger.info("Run hello coroutine...")
    return {"message": "Hello, FastAPI"}
