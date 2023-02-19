import json

from ..models import CakeInOven


def handler(event, context):
    cake: CakeInOven = CakeInOven()
    return {
        "statusCode": 201,
        "body": json.dumps(cake.dict()),
    }


def handler_v2(event, context):
    cake: CakeInOven = CakeInOven()
    return {
        "statusCode": 201,
        "body": json.dumps(cake.dict()),
    }
