import logging

from fastapi import APIRouter
from src.models import UserCreate, UserRead, UserDocument, GroupCreate, GroupRead, GroupDocument

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/")
async def hello():
    logger.info("Run hello coroutine...")
    return {"message": "Hello, FastAPI"}


@router.get("/groups/", response_model=list[GroupRead])
async def get_groups():
    groups = await GroupDocument.find().to_list()
    return groups


@router.post("/groups/", response_model=GroupRead)
async def create_group(group_create: GroupCreate):
    group_doc = GroupDocument(
        name=group_create.name,
        description=group_create.description,
    )
    group_read = await group_doc.insert()
    return group_read


@router.get("/users", response_model=list[UserRead])
async def users():
    users_doc = await UserDocument.find().to_list()
    users_read = []
    for user_doc in users_doc:
        users_read.append(
            UserRead(
                email=user_doc.email,
                first_name=user_doc.first_name,
                last_name=user_doc.last_name,
                groups=[g.name for g in user_doc.groups]
            )
        )
    return users_read


@router.post("/users", response_model=UserRead)
async def users(user_create: UserCreate):
    user_doc = UserDocument(
        email=user_create.email,
        first_name=user_create.first_name,
        last_name=user_create.last_name
    )
    user_doc = await user_doc.insert()
    user_read = UserRead(
        email=user_doc.email,
        first_name=user_doc.first_name,
        last_name=user_doc.last_name,
        groups=[g.name for g in user_doc.groups]
    )
    return user_read
