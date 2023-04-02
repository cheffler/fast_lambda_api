import json
from typing import Any, Dict, Optional, Tuple, Union, get_args

import yaml
from click import UsageError
from fastapi import FastAPI
from fastapi.routing import APIRoute
from pydantic import AnyUrl
from starlette.routing import Mount, Route
from yaml import Dumper

from src.app import custom_openapi
from src.constants import PRIVATE_API_KEY

from .config import config

AllPossibleRouteClasses = Union[Route, APIRoute, Mount]


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


def is_route_private(
    route: Route,
) -> bool:
    if not getattr(route, "openapi_extra", False):
        return False

    return getattr(route, "openapi_extra").get(
        PRIVATE_API_KEY,
        False,
    )


def get_filtered_private_spec(
    app: FastAPI,
) -> Tuple[Dict[str, Any], Optional[Dict[str, Any]]]:
    public_routes = []
    private_routes = []

    route: Any
    classes = get_args(AllPossibleRouteClasses)
    for route in app.routes:
        if isinstance(route, classes):
            if is_route_private(route):
                private_routes.append(route)
            else:
                public_routes.append(route)

    spec: Dict[str, Any] = custom_openapi(routes=public_routes)
    app.openapi_schema = None

    private_spec = custom_openapi(routes=private_routes)
    app.openapi_schema = None

    return spec, private_spec


def get_filtered_spec(
    app: FastAPI, path_filter: str, filter_private: bool = False
) -> Tuple[Dict[str, Any], Optional[Dict[str, Any]]]:
    """
    Create a full OpenAPI spec using a filtered set of APIs.
    """
    filtered_routes = []
    private_routes = []

    classes = get_args(AllPossibleRouteClasses)
    route: Any
    for route in app.routes:
        if isinstance(route, classes):
            if path_filter in route.path:
                if filter_private and is_route_private(route):
                    private_routes.append(route)
                else:
                    filtered_routes.append(route)

    # Use the custom openapi builder from in src/app to get the same tags
    # etc from the app
    spec: Dict[str, Any] = custom_openapi(routes=filtered_routes)

    # clear spec after being used, to support next execution
    app.openapi_schema = None

    private_spec = None
    if filter_private and private_routes:
        private_spec = custom_openapi(routes=private_routes)
        app.openapi_schema = None

    return spec, private_spec
