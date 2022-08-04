from src.data.tests.order_register import OrderRegisterSpy
from src.presentation.http_types.http_response import HttpResponse
from .order_register_controller import OrderRegisterController


class HttpRequestMock():
    def __init__(self) -> None:
        self.body = {
            "some_variable": "some_data"
        }


def test_handler():
    http_request_mock = HttpRequestMock()
    use_case = OrderRegisterSpy()
    order_register_controller = OrderRegisterController(use_case)

    response = order_register_controller.handle(http_request_mock)

    assert use_case.register_order_attributes["data"] == http_request_mock.body

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"]["attributes"] is not None
