from src.infra.db.tests.orders_repository import OrdersRepositorySpy
from .order_register import OrderRegister


def test_order_register():
    repo = OrdersRepositorySpy()
    order_register = OrderRegister(repo)

    mock_data = {"my_data": "some_data"}

    response = order_register.register_order(mock_data)

    assert repo.register_order_attributes["data"] == mock_data

    assert "data" in response
