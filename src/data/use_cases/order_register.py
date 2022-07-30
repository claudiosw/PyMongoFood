from typing import Dict
from src.data.interfaces.orders_repository import OrdersRepositoryInterface
from src.domain.use_cases.order_register import OrderRegister as OrderRegisterInterface


class OrderRegister(OrderRegisterInterface):
    def __init__(self, order_repository: OrdersRepositoryInterface) -> None:
        self.__order_repository = order_repository

    def register_order(self, data: Dict) -> Dict:
        order = self.__order_repository.register_order(data)
        if not order:
            raise Exception('Order Not Created')

        return self.__format_response(order)

    def __format_response(self, data: Dict) -> Dict:
        return {
            "data": data
        }
