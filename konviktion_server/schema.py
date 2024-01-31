from typing import Any, AsyncGenerator, Type

import strawberry
import strawberry_django
from authentikate.strawberry.permissions import HasScopes, IsAuthenticated, NeedsScopes
from kante.directives import relation, replace, upper
from kante.types import Info
from koherent.strawberry.extension import KoherentExtension
from strawberry import ID
from strawberry.field_extensions import InputMutationExtension
from strawberry.permission import BasePermission
from strawberry_django.optimizer import DjangoOptimizerExtension

from bridge import models, mutations, queries, types
from bridge.channel import image_listen
from bridge.conn import NotionExtension


@strawberry.type
class Query:
    omero_users: list[types.NotionIntegration] = strawberry_django.field(extensions=[])
    databases: list[types.Database] = strawberry.field(resolver=queries.databases)
    database = strawberry.field(resolver=queries.database)
    users: list[types.NotionUser] = strawberry.field(resolver=queries.users)
    user = strawberry.field(resolver=queries.user)
    
    me: types.User = strawberry.field(resolver=queries.me)
    


@strawberry.type
class Mutation:
    ensure_integration: types.NotionIntegration = strawberry_django.mutation(
        resolver=mutations.ensure_integration,
    )
    


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    directives=[upper, replace, relation],
    extensions=[
        DjangoOptimizerExtension,
        KoherentExtension,
        NotionExtension
    ],
)
