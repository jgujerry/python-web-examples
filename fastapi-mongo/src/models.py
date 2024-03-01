from beanie import Document, Link
from pydantic import BaseModel


class Group(BaseModel):
    name: str
    description: str


class User(Document):
    email: str
    first_name: str = None
    last_name: str = None
    groups: list[Link[Group]]
