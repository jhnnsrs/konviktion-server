import strawberry
import strawberry.django
from strawberry import auto
from typing import List, Optional, Annotated, Union, cast
import strawberry_django
from bridge import models, scalars, filters, enums, basemodels
from django.contrib.auth import get_user_model
from koherent.models import AppHistoryModel
from authentikate.strawberry.types import App
from kante.types import Info
import datetime

from itertools import chain
from enum import Enum
from strawberry.experimental import pydantic
from pydantic import BaseModel

@strawberry_django.type(get_user_model())
class User:
    id: auto
    sub: str
    username: str
    email: str
    password: str

    @strawberry_django.field
    def integrations(self) -> list["NotionIntegration"]:
        return models.NotionIntegration.objects.filter(user=self).all()
    

@pydantic.type(basemodels.PersonModel)
class Person:
    email: str | None = None



@pydantic.type(basemodels.DatabaseModel)
class Database:
    id: str
    created_time: datetime.datetime
    title: str
    description: str


    
@pydantic.type(basemodels.NotionUserModel)
class NotionUser:
    id: str
    type: str
    person: Person | None = None


@strawberry_django.type(models.NotionIntegration)
class NotionIntegration:
    id: auto
    notion_token: str
    user: User