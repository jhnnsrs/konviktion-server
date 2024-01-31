from .models import NotionIntegration
from contextlib import contextmanager
from django.conf import settings
from contextvars import ContextVar
from strawberry.extensions import SchemaExtension
from asgiref.sync import sync_to_async
from notion_client import AsyncClient

current_conn: ContextVar[AsyncClient] = ContextVar("current_conn")

@sync_to_async
def get_integration(context):
    if not context.request.user.is_authenticated:
        raise Exception("User is not authenticated")

    user = NotionIntegration.objects.filter(user=context.request.user).first()
    return user


def get_conn() -> AsyncClient:
    try:
        return current_conn.get()
    except LookupError:
        raise Exception("No OMERO connection found")

class NotionExtension(SchemaExtension):
    async def on_operation(self):
        print("Starting operation")
        try:
            user = await get_integration(self.execution_context.context)
            print(user)

            conn = AsyncClient(auth=user.notion_token)
            token = current_conn.set(conn)

            try:
                yield
            finally:
                current_conn.reset(token)
        except Exception as e:
            print(e)
            yield
