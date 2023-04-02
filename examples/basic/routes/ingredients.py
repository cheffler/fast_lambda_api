# flake8: noqa: E501

from typing import Dict

from fastapi import APIRouter, Path, Query, Request

from examples.basic.models.cake import Ingredient, Ingredients
from src import PRIVATE_API_KEY, import_handler

OPENAPI_TAG_NAME: str = "Ingredient APIs"
OPENAPI_TAG: Dict[str, str] = {
    "name": OPENAPI_TAG_NAME,
    "description": """Ingredients are core to the service, so only the GET APIs are made public, the others are all private.
    
    Private APIs only accessible to services, systems and applications within the Organisations VPC or with VPN access to the same""",
}

ingredient_api_v1: APIRouter = APIRouter(prefix="/v1", tags=[OPENAPI_TAG_NAME])


@ingredient_api_v1.get("/ingredient", response_model=Ingredients)
@import_handler(path="examples.basic.lambdas.ingredients")
def get_ingredients(
    request: Request, type=Query(description="The type of ingredient to search for")
):
    """Gets a list of Ingredients based on query params"""
    ...


@ingredient_api_v1.post(
    "/ingredient",
    response_model=Ingredient,
    status_code=201,
    openapi_extra={PRIVATE_API_KEY: True},
)
@import_handler(path="examples.basic.lambdas.ingredients")
def create_ingredient(request: Request, ingredient: Ingredient):
    """
    Only systems within the VPC can create new ingredients
    """
    ...


@ingredient_api_v1.get("/ingredient/{id}", response_model=Ingredient)
@import_handler(path="examples.basic.lambdas.ingredients")
def get_ingredient(
    request: Request,
    id: str = Path(
        regex="^ing_\w{22}$",
        description="The unique ID for of the ingredient to update",
    ),
):
    """Gets an Ingredient by id"""
    ...


@ingredient_api_v1.put(
    "/ingredient/{id}",
    response_model=Ingredient,
    openapi_extra={PRIVATE_API_KEY: True},
)
@import_handler(path="examples.basic.lambdas.ingredients")
def update_ingredient(
    request: Request,
    ingredient: Ingredient,
    id: str = Path(
        regex="^ing_\w{22}$",
        description="The unique ID for of the ingredient to update",
    ),
):
    """
    Only systems within the VPC can update ingredients
    """
    ...


@ingredient_api_v1.delete(
    "/ingredient/{id}",
    openapi_extra={PRIVATE_API_KEY: True},
)
@import_handler(path="examples.basic.lambdas.ingredients")
def remove_ingredient(
    request: Request,
    id: str = Path(
        regex="^ing_\w{22}$",
        description="The unique ID for of the ingredient to update",
    ),
):
    """
    Only systems within the VPC can delete ingredients
    """
    ...
