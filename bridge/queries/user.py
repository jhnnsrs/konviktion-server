from bridge.conn import get_conn
from bridge import types, filters, basemodels
from strawberry_django import pagination
import strawberry

async def users(filters: filters.ProjectFilter | None = None, pagination: pagination.OffsetPaginationInput | None = None) -> list[types.NotionUser]:
    x = await get_conn().users.list()
    result = x.get("results")
    print(result)
    return [basemodels.NotionUserModel(**y) for y in result]


async def user(id: strawberry.ID) -> types.Database:
    x = await get_conn().databases.retrieve(id)
    return types.Database(value=x)