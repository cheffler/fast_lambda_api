from typing import Optional, List, Dict, Union, Any
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


app: FastAPI = FastAPI()

openapi_custom_details: dict = {}
additional_custom_details: dict = {}


def customise_openapi_schema(
    title: str = "OpenAPI Specification for AWS API Gateway",
    version: str = "0.0.1",
    openapi_version: str = app.openapi_version,
    description: Optional[str] = None,
    tags: Optional[List[Dict[str, str]]] = None,
    servers: Optional[List[Dict[str, Union[str, Any]]]] = None,
    logo_url: Optional[str] = None,
) -> None:
    """
    Customise the OpenAPI specification with additional details
    """
    global openapi_custom_details
    global additional_custom_details

    openapi_custom_details = {
        "title": title,
        "version": version,
        "openapi_version": openapi_version,
        "description": description,
        "tags": tags,
        "servers": servers,
    }

    additional_custom_details = {"logo_url": logo_url}


def custom_openapi():
    global openapi_custom_details
    global additional_custom_details

    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        **openapi_custom_details,
        routes=app.routes,
    )

    if additional_custom_details.get("logo_url"):
        openapi_schema["info"]["x-logo"] = {
            "url": additional_custom_details.get("logo_url")
        }

    app.openapi_schema = openapi_schema

    return app.openapi_schema


app.openapi = custom_openapi
