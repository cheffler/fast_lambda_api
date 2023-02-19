from importlib import import_module
from types import ModuleType
from fastapi import FastAPI


def load_app(module: str, app_name: str) -> FastAPI:
    module = module.replace("/", ".").strip(".py")
    handler_module: ModuleType = import_module(module)

    return getattr(handler_module, app_name)
