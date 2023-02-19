import json
from typing import Any, Union, get_args

import yaml
from click import UsageError
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.routing import APIRoute
from pydantic import AnyUrl
from starlette.routing import Mount, Route
from yaml import Dumper

from .config import config


def any_url_representer(dumper: Dumper, data: AnyUrl):
    """
    yaml representer to handle the AnyUrl class
    """
    return dumper.represent_str(data)


def format_spec(spec: dict, format: str):
    """
    Format the specification to the target format
    """
    if format == "json":
        return json.dumps(
            spec,
            sort_keys=False,
            indent=config.default_json_spaces,
            default=str,
        )

    if format == "yaml":
        yaml.add_representer(AnyUrl, any_url_representer)
        return yaml.dump(
            spec,
            indent=config.default_yaml_spaces,
            sort_keys=False,
        )

    raise UsageError(f"File format {format} is not supported")


def filter_paths_in_app(app: FastAPI, path_contains: str):
    filtered_routes = []
    classes = get_args(Union[Route, APIRoute, Mount])
    route: Any
    for route in app.routes:
        if isinstance(route, classes):
            if path_contains in route.path:
                filtered_routes.append(route)

    app.openapi_schema = None

    return get_openapi(
        title=app.title,
        version=app.version,
        openapi_version=app.openapi_version,
        description=app.description,
        tags=app.openapi_tags,
        servers=app.servers,
        terms_of_service=app.terms_of_service,
        contact=app.contact,
        license_info=app.license_info,
        routes=filtered_routes,
    )
