from pydantic import BaseModel
from typing import Literal, Optional
import datetime

class DatabaseModel(BaseModel):
  object: Literal["database"]
  id: str
  created_time: datetime.datetime
  title: str
  description: str


class PersonModel(BaseModel):
  email: str | None = None

class NotionUserModel(BaseModel):
  object: Literal["user"]
  type: str
  avatar_url: str | None = None
  person: PersonModel | None = None
  id: str
