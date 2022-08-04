from src.infra.db.settings import db_connection_handler
from .orders_repository import OrdersRepository


db_connection_handler.connect_to_db()


def test_register_order():
    orders_repository = OrdersRepository()
    fake_registry = {
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
    database = db_connection_handler
    collection = database.get_collection('order')
    collection.delete_one({"_id": "test"})
    collection = database.get_collection('order')
    orders_repository.register_order(fake_registry)
    order = collection.find_one({"_id": "test"})
    collection.delete_one({"_id": "test"})
    assert order == fake_registry
