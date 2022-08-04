def create_mock_order():
    return {
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
