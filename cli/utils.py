import json
from importlib import import_module
from types import ModuleType

import yaml
from click import UsageError
from fastapi import FastAPI
from pydantic import AnyUrl
from yaml import Dumper

from .config import config


def load_app(module: str, app_name: str) -> FastAPI:
    """
    Load a FastAPI application from the target module and app
    """
    module = module.replace("/", ".").strip(".py")
    handler_module: ModuleType = import_module(module)

    return getattr(handler_module, app_name)


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
