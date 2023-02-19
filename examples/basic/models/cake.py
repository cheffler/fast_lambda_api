# flake8: noqa: E501

from enum import Enum
from random import randint
from typing import List, Optional, Union
from uuid import uuid4

from pydantic import BaseModel, Field


def str_uuid_v4() -> str:
    return str(uuid4())


def rand_int() -> int:
    return randint(1, 100)


class TypesOfCake(str, Enum):
    SPONGE: str = "sponge"
    LAYER: str = "layer"
    GENOISE: str = "Genoise"
    CHIFFON: str = "Chiffon"
    ANGEL: str = "Angel"
    FLOURLESS: str = "Flourless"
    UPSIDE_DOWN: str = "Upside-Down"
    DEVILS: str = "Devil’s"
    FRUIT: str = "Fruit"


class Units(str, Enum):
    ML: str = "ml"
    LITRE: str = "litre"
    CUP: str = "cup"
    GALLON: str = "gallon"
    TBL: str = "tbl"
    TBSP: str = "tbsp"
    GRAMS: str = "grams"
    NUMBER: str = "number"


class Ingredient(BaseModel):
    name: str = Field(description="The name of the ingredient")
    quantity: Union[int, str] = Field(description="The amount of the ingredient")
    unit: Units = Field(description="The unit the quantity is measured in")


class Temperature(BaseModel):
    celsius: int
    fahrenheit: int


class CakeRecipe(BaseModel):
    class Config:
        schema_extra: dict = {
            "example": {
                "name": "Victoria Sponge",
                "type": "sponge",
                "prep_time": 20,
                "bake_time": 40,
                "ingredients": [
                    {"name": "flour", "quantity": 500, "unit": "grams"},
                    {"name": "eggs", "quantity": 2, "unit": "number"},
                ],
                "oven_temp": {
                    "celsius": 200,
                    "fahrenheit": 392,
                },
                "steps": [
                    "Mix all ingredients",
                    "Grease cake tin",
                    "Put mix into cake tin",
                    "Bake for 40 minutes",
                    "Remove and let cool before decorating",
                ],
            }
        }

    name: str = Field(description="The name of the cake")
    type: TypesOfCake = Field(description="The type of cake")
    prep_time: int = Field(
        0, description="The number of minutes needed for preparation"
    )
    bake_time: int = Field(
        0, description="The number of minutes needed to cook the cake"
    )
    setting_time: int = Field(
        0, description="The amount of minutes this cake needs in the fridge or to set"
    )
    ingredients: List[Ingredient] = Field(
        description="The list of ingredients needed for this recipe"
    )
    oven_temp: Optional[Temperature] = Field(
        description="The temperature the oven needs to be on, if the oven is required"
    )
    steps: List[str] = Field(description="The steps needed to prepare this cake")


class SavedCakeRecipe(CakeRecipe):
    id: str = Field(description="The ID of this recipe in the system")


class CakeById(BaseModel):
    id: str = Field(description="The ID of the cake you want to make")


class CakeInOven(BaseModel):
    id: str = Field(
        default_factory=str_uuid_v4,
        description="The id of the cake going through the baking process",
    )
    place_in_queue: int = Field(
        default_factory=rand_int,
        description="The position of the cake in the baking queue",
    )
