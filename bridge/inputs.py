from typing import List, Optional

import strawberry
import strawberry_django
from django.conf import settings
from pydantic import BaseModel
from strawberry import ID, field
from strawberry.experimental import pydantic

from bridge import models


class EnsureIntegrationInputModel(BaseModel):
    token: str
    workspace: str


@pydantic.input(EnsureIntegrationInputModel)
class EnsureIntegration:
    token: str
    workspace: str 



class CreateProjectInputModel(BaseModel):
    name: str
    description: str | None = None

@pydantic.input(CreateProjectInputModel)
class CreateProjectInput:
    name: str
    description: str | None = None