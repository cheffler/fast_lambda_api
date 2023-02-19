# Fast Lambda API

This is a development dependency library to support the developer experience of working in an API First process with AWS Lambdas and AWS API Gateway.

It has two main objectives:

- Support the creation of an OpenAPI spec from Code that is comprehensive and supports AWS API Gateway operations
- Provide a local simple API handler that mimics, very simply, the Lambda environment to speed of development

The basis of this tooling is the OpenAPI specification portability and can provide advantages in a number of different scenarios. The spec can be used to:

- Create an AWS API Gateway
- Generate interactive documentation for your APIs
- Autogenerate and SDK in a number of languages to empower clients to use your API
- Be injected into Postman and other API tools

The tooling provides a place to create and document APIs powered by document enriched models, these APIs can be decorated to link a Lambda handler.

This library is a development only tool, therefore it does not provide any tooling to help with the Lambda handlers or more. There are a few good libraries out there to provide frameworks for your Lambda code, one in particular is [AWS Lambda Powertools](https://awslabs.github.io/aws-lambda-powertools-python).

## Use Cases

- API First
- Create an API spec
- OpenAPI Spec to create API Gateway
- Alternatives to using the Spec

## Features

- [x] Decorator to access handler
- [x] Standard FastAPI app to inject routes
- [x] Configure OpenAPI spec
- [x] Add tags
- [ ] CLI tooling
  - [x] Extract
  - [ ] Extract for API Gateway
  - [ ] Extract for Docs
  - [ ] Filter APIs (duplicate task)
  - [ ] Bootstrap
  - [ ] Template router
  - [ ] Inject route
  - [ ] Link to [setuptools](https://click.palletsprojects.com/en/8.1.x/setuptools/), other [reference](https://pybit.es/articles/how-to-package-and-deploy-cli-apps/)
- [ ] Extend OpenAPI spec with AWS security examples
- [ ] Examples
  - [ ] Basic
  - [ ] Lambdalith
- [ ] CI/CD and publish library
- [ ] Decorator/code to inject lambda into API Spec
- [ ] Split API spec by version
- [ ] Split API spec by private/public
- [ ] Strip API spec(s) for documentation sites, e.g. remove AWS specific info
- [ ] Helpers for AWS API Gateway "things"
- [ ] Template/class for headers of API spec, e.g. servers, info, etc
- [ ] Events and event API specs
- [ ] Refresh import cache on header
- [ ] Handle different paths, dot and slash notation
- [ ] Check if FastAPI validation works & document
- [ ] More documentation
- [ ] Linting tools
- [ ] Unit tests
- [ ] Component tests
- [ ] Add FastAPI lambdalith into routes
