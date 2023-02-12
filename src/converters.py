from fastapi import Request
from uuid import uuid4
from datetime import datetime


def request_to_api_gateway_event(request: Request) -> dict:
    """
    Creates an AWS API Gateway v1 event dictionary from the FastAPI Request
    object

    Args:
        request (Request): The request being passed in

    Returns:
        dict: AWS API Gateway v1 event


    TODO:
    - Cookies
    - authorizer "stuff"
    """

    headers = dict(request.headers.raw)
    query_params = request.query_params._dict
    path = request.url.path
    method = request.method

    if hasattr(request, "_body"):
        body = request._body
    else:
        body = None

    source_ip = None
    if request.client:
        source_ip = request.client.host

    return {
        "version": "1.0",
        "resource": path,
        "path": path,
        "httpMethod": method,
        "headers": headers,
        "multiValueHeaders": {},
        "queryStringParameters": query_params,
        "multiValueQueryStringParameters": query_params,
        "pathParameters": request.path_params,
        "stageVariables": None,
        "body": body,
        "isBase64Encoded": False,
        "requestContext": {
            "path": "/dev/",
            "accountId": "123456789012",
            "resourceId": "123456789012",
            "stage": "dev",
            "requestId": str(uuid4()),
            "domainName": "id.execute-api.eu-west-1.amazonaws.com",
            "domainPrefix": "id",
            "extendedRequestId": "request-id",
            "httpMethod": method,
            "protocol": "HTTP/1.1",
            "requestTime": datetime.now().strftime(
                "%d/%b/%Y:%H:%M:%S %z"
            ),  # "04/Mar/2020:19:15:17 +0000"
            "requestTimeEpoch": datetime.now().timestamp(),
            "resourcePath": path,
            "authorizer": {"claims": None, "scopes": None},
            "identity": {
                "accessKey": None,
                "accountId": None,
                "caller": None,
                "cognitoAuthenticationProvider": None,
                "cognitoAuthenticationType": None,
                "cognitoIdentityId": None,
                "cognitoIdentityPoolId": None,
                "principalOrgId": None,
                "sourceIp": source_ip,
                "user": None,
                "userAgent": request.headers.get("user-agent"),
                "userArn": None,
                "clientCert": {
                    "clientCertPem": "CERT_CONTENT",
                    "subjectDN": "www.example.com",
                    "issuerDN": "Example issuer",
                    "serialNumber": "a1",
                    "validity": {
                        "notBefore": "May 28 12:30:02 2019 GMT",
                        "notAfter": "Aug  5 09:36:04 2021 GMT",
                    },
                },
            },
            "apiId": "j3azlsj0c4",
        },
    }
