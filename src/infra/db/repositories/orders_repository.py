from typing import Dict
from src.data.interfaces.orders_repository import OrdersRepositoryInterface
from src.infra.db.settings import db_connection_handler


class OrdersRepository(OrdersRepositoryInterface):

    @classmethod
    def register_order(cls, data: Dict) -> Dict:
        database = db_connection_handler
        collection = database.get_collection('order')
        new_order = collection.insert_one(data)
        return str(new_order.inserted_id)
