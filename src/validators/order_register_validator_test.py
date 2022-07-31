# pylint: disable=bare-except
# pylint: disable=comparison-of-constants
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from .order_register_validator import order_register_validator


class MockRequest:
    def __init__(self) -> None:
        self.json = None


def test_order_register_validator():
    request = MockRequest()
    request.json = {
        "_id": "test",
        "client": "Joseph Test",
        "address": "Olive Trees Street",
        "items": [
            {
                "item": "hamburguer",
                "price": 18.90,
                "side_dish": "mustard"
            },
            {
                "item": "Sushi",
                "price": 29.50,
                "side_dish": "sauce"
            },
        ]
    }

    try:
        order_register_validator(request)
    except:
        assert False


def test_order_register_validator_with_error():
    request = MockRequest()
    request.json = {}

    try:
        order_register_validator(request)
        assert False
    except Exception as exception:
        assert isinstance(exception, HttpUnprocessableEntityError)
