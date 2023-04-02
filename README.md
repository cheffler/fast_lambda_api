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

## Getting Started

> this section explains how to get started and work with this repo, using the library in other projects will come in time...

This repo uses `Python3`, `pyenv` and `pipenv` as a base, so have these installed and be familiar how to use them on a basic level (that's all I know anyway)

```sh
# setup virtual env and install dependencies
pipenv install
```

```sh
# Run the basic example
pipenv run basic

# swagger like docs are available at localhost:8000/docs
# redocly like docs are available at localhost:8000/redoc
```

### CLI Commands

Below are some working examples of the CLI commands built to-date

| Command | Description | Example |
|----|----|----|
| `pipenv run basic`| Run the basic example ||
| `pipenv run cli export --help`| View the help for the export CLI|
| `pipenv run cli export --filter v1` | Export an API spec filtering for APIs|`pipenv run cli export -t examples/basic/main.py --filter v2`|
| `pipenv run cli export -p` | Export private APIs to separate files||

## Use Cases

- API First
- Create an API spec
- OpenAPI Spec to create API Gateway
- Alternatives to using the Spec

## Features

### Main

- [x] Decorator to access handler
- [x] Standard FastAPI app to inject routes
- [x] Add OpenAPI spec tags
- [x] Private tag on extras
- [ ] Not Implemented decorator
- [ ] Security decorator
- [ ] WIP decorator
- [ ] [Extend OpenAPI](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions.html) spec with AWS security examples
- [ ] Decorator/code to inject lambda into API Spec
- [ ] Helpers for AWS API Gateway "things"
- [ ] Events and event API specs
- [ ] Refresh import cache on header
- [ ] Add FastAPI lambdalith into routes
- [ ] Handle different paths, dot and slash notation in handler decorator
- [ ] More documentation

### Configuration

- [x] Configure OpenAPI spec
- [x] Basic config class
- [ ] Configure the custom names of spec properties
- [ ] Configure target folders etc
- [ ] Names
- [ ] Basic OpenAPI configuration in a file
- [ ] Config from JSON, ini, yaml, pyproject.toml
- [ ] Template/class for headers of API spec, e.g. servers, info, etc

### CLI tooling

- [x] Extract
- [x] Split API spec by version
- [x] Filter APIs (duplicate task)
- [ ] Split API spec by private/public
- [ ] Strip API spec(s) for documentation sites, e.g. remove AWS specific info
- [ ] Extract for API Gateway
- [ ] Extract for Docs
- [ ] Bootstrap
- [ ] Template router
- [ ] Inject route
- [ ] Link to [setuptools](https://click.palletsprojects.com/en/8.1.x/setuptools/), other [reference](https://pybit.es/articles/how-to-package-and-deploy-cli-apps/)
- [ ] Export to Postman
- [ ] Merge with other OpenAPI spec

### Examples

- [ ] Basic
  - [x] Public
  - [x] Private
  - [ ] Not implemented
  - [ ] Templated response from AWS Gateway (&ß local)
- [ ] V1 & V2
- [ ] Lambdalith

### Testing & CI/CD

- [ ] Build in GH actions
- [ ] Add publishing of library
- [ ] Linting tools
- [ ] Unit tests
- [ ] Component tests
- [ ] Check if FastAPI validation works & document

## References

- [AWS OpenAPI specification extensions](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions.html)
