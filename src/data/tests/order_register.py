from typing import Dict
from src.domain.tests.orders import create_mock_order


class OrderRegisterSpy:
    def __init__(self) -> None:
        self.register_order_attributes = {}

    def register_order(self, data: Dict) -> Dict:
        self.register_order_attributes["data"] = data
        return create_mock_order
