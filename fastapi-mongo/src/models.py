import pymongo
from beanie import Document, Link
from pydantic import BaseModel
from pymongo import IndexModel


class GroupCreate(BaseModel):
    name: str
    description: str = None


class GroupRead(GroupCreate):
    pass


class GroupDocument(GroupRead, Document):
    pass

    class Settings:
        name = "groups"
        indexes = [
            IndexModel(
                [("name", pymongo.ASCENDING)],
                unique = True
            )
        ]


class UserCreate(BaseModel):
    email: str
    first_name: str = None
    last_name: str = None


class UserRead(UserCreate):
    groups: list[str]



class UserDocument(UserRead, Document):
    groups: list[Link[GroupDocument]] = []

    class Settings:
        name = "users"
        indexes = [
            IndexModel(
                [("email", pymongo.ASCENDING)],
                unique = True
            )
        ]
