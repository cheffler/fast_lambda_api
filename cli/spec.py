import json
from typing import Any, Dict, Union, get_args

import yaml
from click import UsageError
from fastapi import FastAPI
from fastapi.routing import APIRoute
from pydantic import AnyUrl
from starlette.routing import Mount, Route
from yaml import Dumper

from src.app import custom_openapi

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


def get_filtered_spec(app: FastAPI, path_contains: str) -> Dict[str, Any]:
    """
    Create a full OpenAPI spec using a filtered set of APIs.
    """
    filtered_routes = []
    classes = get_args(Union[Route, APIRoute, Mount])
    route: Any
    for route in app.routes:
        if isinstance(route, classes):
            if path_contains in route.path:
                filtered_routes.append(route)

    # Use the custom openapi builder from in src/app to get the same tags
    # etc from the app
    spec: Dict[str, Any] = custom_openapi(routes=filtered_routes)

    # clear spec after being used, to support next execution
    app.openapi_schema = None

    return spec
