from typing import Type
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.domain.use_cases.order_register import OrderRegister as OrderRegisterInterface


class OrderRegisterController(ControllerInterface):
    def __init__(self, use_case: Type[OrderRegisterInterface]) -> None:
        self.__use_case = use_case

    def handle(self, http_request: Type[HttpRequest]) -> Type[HttpResponse]:
        data = http_request.body
        response = self.__use_case.register_order(data)

        return HttpResponse(
            status_code=200,
            body={
                "data": {
                    "type": "Orders",
                    "count": 1,
                    "attributes": response,
                }
            }
        )
