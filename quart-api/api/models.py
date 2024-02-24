from typing import List
from pydantic import BaseModel


class User(BaseModel):
  username: str
  email: str


class Team(BaseModel):
  users: List[User]
