from src.infra.db.repositories.orders_repository import OrdersRepository
from src.data.use_cases.order_register import OrderRegister
from src.presentation.controllers.order_register_controller import OrderRegisterController


def order_register_composer():
    repository = OrdersRepository
    use_case = OrderRegister(repository)
    controller = OrderRegisterController(use_case)

    return controller
