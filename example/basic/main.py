from src import app, customise_openapi_schema
from .routes.commands import (
    commands_api_v1,
    commands_api_v2,
    OPENAPI_TAG as command_tags,
)
from fastapi.staticfiles import StaticFiles
from .desc import MAIN_DESCRIPTION


customise_openapi_schema(
    title="Basic Example of Lambda API Gateway",
    version="0.1.0",
    description=MAIN_DESCRIPTION,
    tags=[command_tags],
    servers=[
        {
            "url": "http://localhost:8000",
            "description": "Local server",
        }
    ],
    logo_url="http://localhost:8000/static/logo_black.png",
)

# To enable the logo, mount a static directory
app.mount(
    "/static",
    StaticFiles(directory="example/basic/static"),
    name="static",
)


app.include_router(commands_api_v1)
app.include_router(commands_api_v2)
