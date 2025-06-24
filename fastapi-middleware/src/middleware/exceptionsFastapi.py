"""fastapi exception handlers"""
from typing import Union

from fastapi import HTTPException as Fastapi_HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.openapi.constants import REF_PREFIX
from fastapi.openapi.utils import validation_error_response_definition
from pydantic import ValidationError
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from utils import rnd

validation_error_response_definition["properties"] = {
    "errors": {
        "title": "Errors",
        "type": "array",
        "items": {"$ref": "{0} ValidationError".format(REF_PREFIX)},
    },
}


async def parameters_error(
    request: Request, exc: Union[RequestValidationError, ValidationError]
):
    content = jsonable_encoder({"errors": exc.errors(), "body": exc.body})
    return JSONResponse(
        {
            "detail": f"Handled 'parameters_error' with detail => {content} ",
            "fname": f"{request.state.fname}",
            "random": f"{rnd()}",
        },
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
    )


async def not_found(request: Request, exc: HTTPException):
    return JSONResponse(
        {
            "detail": "404 fat fingers... maybe?",
            "fname": f"{request.state.fname}",
            "random": f"{rnd()}",
        },
        status_code=exc.status_code,
    )


async def server_error(request: Request, exc: HTTPException):
    return JSONResponse(
        {
            "detail": "Handled 'server_error': "
            "What have you done? You broke my beautiful web-service !!",
            "fname": f"{request.state.fname}",
            "random": f"{rnd()}",
        },
        status_code=exc.status_code,
    )


async def http_exception(request: Request, exc: Fastapi_HTTPException):
    return JSONResponse(
        {
            "detail": f"Handled 'http_exception' with detail -> {exc.detail}",
            "fname": f"{request.state.fname}",
            "random": f"{rnd()}",
        },
        status_code=exc.status_code,
    )
