from importlib import import_module

from functools import wraps
import json
from types import ModuleType
from typing import Callable
from fastapi import HTTPException, Request

from .converters import request_to_api_gateway_event


def import_handler(
    *args,
    path: str,
    handler: str = "handler",
):
    """
    Decorator for a FastAPI Route that imports and invokes a Python Lambda handler.
    Decorator with within the FastAPI tooling and requires the kwarg of `request` to be present in the route handler (`get_things` below). Formats the FastAPI request into an AWS API Gateway Event, converts to JSON and calls the handler. Handler is invoked by this decorator, so no need to add any custom logic.

    Example:
    ```
    @app.get("/things")
    @import_handler(
        path="path.to.file",
        handler="name_of_method_in_file"
    )
    def get_things(request: Request):
        ...
    ```

    Args:
        path (str): The path, using module import style, to the file for
        the handler. Use absolute paths starting with a module that is
        "findable" on the PYTHONPATH.
        handler (str, optional): The actual method in the module to
        invoke. Defaults to "handler".
    """

    def inner(func):
        @wraps(func)
        def inject_handler(*args, request: Request, **kwargs):
            handler_module: ModuleType = import_module(path)
            handler_func: Callable = getattr(handler_module, handler)

            event: dict = request_to_api_gateway_event(request)

            res: dict = handler_func(event, {})
            status_code: int = res["statusCode"]
            data: dict = json.loads(res["body"])

            if status_code >= 400:
                raise HTTPException(
                    status_code=status_code,
                    detail=data["detail"],
                )

            return data

        return inject_handler

    return inner
