from src import app
from .routes.commands import (
    commands_api_v1,
    commands_api_v2,
    OPENAPI_TAG as command_tags,
)

app.openapi_tags = [command_tags]

app.include_router(commands_api_v1)
app.include_router(commands_api_v2)
