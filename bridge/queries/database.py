from bridge.conn import get_conn
from bridge import types, filters
from strawberry_django import pagination
import strawberry

async def databases(filters: filters.ProjectFilter | None = None, pagination: pagination.OffsetPaginationInput | None = None) -> list[types.NotionUser]:
    x = await get_conn().databases.list()
    print(x)
    return [types.Database(value=y) for y in x]


async def database(id: strawberry.ID) -> types.NotionUser:
    x = await get_conn().databases.retrieve(id)
    return types.Database(value=x)