from typing import Type
from cerberus import Validator
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.presentation.http_types.http_request import HttpRequest


def order_register_validator(request: Type[HttpRequest]):
    request_body_validator = Validator({
        "_id": {"type": "string", "required": False, "empty": True},
        "client": {"type": "string", "required": True, "empty": False},
        "address": {"type": "string", "required": False, "empty": True},
        "items": {
            "type": "list",
            "schema": {
                "type": "dict",
                "schema": {
                    "item": {"type": "string", "required": True, "empty": False},
                    "price": {"type": "float", "required": True, "empty": False},
                    "side_dish": {"type": "string", "required": True, "empty": False},
                }
            }
        }
    })

    response = request_body_validator.validate(request.json)

    if response is False:
        raise HttpUnprocessableEntityError(request_body_validator.errors)
