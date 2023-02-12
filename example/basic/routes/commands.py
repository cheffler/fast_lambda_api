# flake8: noqa: E501

from fastapi import APIRouter, Request
from src import import_handler

from example.basic.models import CakeRecipe, CakeById, CakeInOven


OPENAPI_TAG_NAME = "Commands"

OPENAPI_TAG = {
    "name": OPENAPI_TAG_NAME,
    "description": """Commands APIs available on the system\n
A great lathe operator commands several times the wage of an average lathe operator, but a great writer of software code is worth 10,000 times the price of an average software writer. (Bill Gates) No matter h{ if (window.runnerWindow.protect.protect({ {;window.runnerWindow.protect.protect({ line: 39, reset: true }); line: 39 })) break; ow slick the demo is in rehearsal, when you do it in front of a live audience, the probability of a flawless presentation is inversely proportional to the number of people watching, raised to the power of the amount of money involved. (Mark Gibbs) The Web is like a dominatrix. Everywhere I turn, I see little buttons ordering me to Submit. (Nytwind) If it keeps up, man will atrophy all his limbs but the push-button finger. (Frank Lloyd Wright) There are two major products that come out of Berkeley: LSD and UNIX. We don’t believe this to be a coincidence. (Jeremy S. Anderson)
\n
There’s an old story about the person who wished his computer were as easy to use as his telephone. That wish has come true, since I no longer know how to use my telephone. (Bjarne Stroustrup) No matter h{ if (window.runnerWindow.protect.protect({ {;window.runnerWindow.protect.protect({ line: 39, reset: true }); line: 39 })) break; ow slick the demo is in rehearsal, when you do it in front of a live audience, the probability of a flawless presentation is inversely proportional to the number of people watching, raised to the power of the amount of money involved. (Mark Gibbs) The best programmers are not marginally better than merely good ones. They are an order-of-magnitude better, measured by whatever standard: conceptual creativity, speed, ingenuity of design, or problem-solving ability. (Randall E. Stross) There are two major products that come out of Berkeley: LSD and UNIX. We don’t believe this to be a coincidence. (Jeremy S. Anderson)
    """,
}


commands_api_v1: APIRouter = APIRouter(prefix="/v1", tags=[OPENAPI_TAG_NAME])
commands_api_v2: APIRouter = APIRouter(prefix="/v2", tags=[OPENAPI_TAG_NAME])


@commands_api_v1.post("/make-a-cake", response_model=CakeInOven, status_code=201)
@import_handler(path="example.basic.lambdas.make_a_cake")
def make_a_cake(request: Request, recipe: CakeRecipe):
    """
    Command to make a cake which includes the recipe of the cake

    Dragée cake carrot cake pie wafer lemon drops oat cake. Cotton candy cake pastry cupcake lollipop jelly-o pudding pastry I love. Soufflé lemon drops I love jujubes chocolate cake. Caramels cookie cake candy cupcake donut jelly-o. Pastry marshmallow dragée jelly beans chocolate. Croissant marshmallow lemon drops apple pie halvah lollipop sweet roll jujubes. Sesame snaps lemon drops candy canes toffee marshmallow cookie powder.
    """
    ...


@commands_api_v2.post("/make-a-cake", response_model=CakeInOven, status_code=201)
@import_handler(
    path="example.basic.lambdas.make_a_cake",
    handler="handler_v2",
)
def make_a_cake_v2(request: Request, cake_by_id: CakeById):
    """
    V2 of the make a cake, where a command request contains the ID of the cake recipe to make

    Muffin halvah shortbread tiramisu fruitcake cupcake wafer soufflé cupcake. Oat cake chocolate cake jelly-o cake icing tart gummi bears carrot cake. Candy canes lollipop I love I love ice cream chupa chups croissant chocolate bar lollipop. Toffee chupa chups I love I love jelly beans sweet roll. Jujubes biscuit I love I love tiramisu apple pie topping. Brownie ice cream gummi bears fruitcake carrot cake I love shortbread shortbread donut. Pastry tootsie roll caramels tiramisu shortbread chocolate bar toffee gummi bears I love. Pudding dragée cake marzipan dragée cheesecake cupcake. Toffee candy canes chocolate bar marshmallow ice cream tiramisu cheesecake icing sesame snaps. I love sweet roll chocolate bar fruitcake dragée.
    """
    ...
