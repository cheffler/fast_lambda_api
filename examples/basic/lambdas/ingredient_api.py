import json


def handler(event, context):
    body = {"message": "You have access a private API"}
    return {
        "statusCode": 201,
        "body": json.dumps(body),
    }
