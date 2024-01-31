from koherent.types import Info
from bridge import types, models, inputs
from django.conf import settings
from notion_client import AsyncClient
import socket


async def ensure_integration(info: Info, input: inputs.EnsureIntegration) -> types.NotionIntegration:


    # lets try if we can reach the omero-server 
    try:
        notion = AsyncClient(auth=input.token)
        list_users_response = await notion.users.list()
        print(list_users_response)

        integration, _ = await models.NotionIntegration.objects.aupdate_or_create(
            user=info.context.request.user,
            workspace=input.workspace,
            notion_token=input.token,
        )

        return integration




    except Exception as e:
        print(e)
        raise Exception("Could not connect to Notion. Please check your token.") from e

