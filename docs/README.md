# Fast Lambda API Dev Tooling

> Explain basic idea

## Features

### Creating OpenAPI Specification

...

### Filtering APIs by Version

...

### Private APIs in AWS

AWS offers a feature of [Private APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-apis.html), allowing you to create a subset of APIs that are only accessible by service, systems, etc within your VPC. This is quite useful for a microservice style architecture where some services are internal only and/or complex behaviour is orchestrated and/or choreographed.

When creating a private API, an entirely separate API Gateway is needed that is ONLY populated by the APIs that are private. Consider this, a microservice has a few APIs that are publicly available and a number of others that are private, but these have a shared domain, data and code base. Using the private flag, as described below, the private APIs can be identified and an OpenAPI specification can be created specifically for the private AWS API Gateway. Furthermore, a separate OpenAPI specification can be used to populate private API documentation that is only available within the organisation.

FastAPI offers a property to add to Routes to inject additional, custom, [details into the OpenAPI specification](https://fastapi.tiangolo.com/advanced/path-operation-advanced-configuration/#openapi-extra), this has been used to flag an API as private.

```py

```
