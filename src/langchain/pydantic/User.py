from typing import List

from pydantic import BaseModel

class User(BaseModel):
        name: str
        age: int
        location: str

class Users(BaseModel):
        users:List[User]