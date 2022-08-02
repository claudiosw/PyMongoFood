# About the project
This is a project to practice PyMongo, testing, design patterns and clean code principles
# Preparing / Installing

### Clone the PyMongoFood repository
```
git clone https://github.com/claudiosw/PyMongoFood.git
```

### Access the project directory:
```
cd PyMongoFood
```

### Create the virtual environment:
```
python -m venv venv

```

### Run the virtual environment:
```
venv\Scripts\activate

```

### Install the required Python packages:
```
pip install -r requirements.txt
pre-commit install
```

### Download [MongoDB](https://www.mongodb.com/try/download/community) and install

# Register order
Run the server
```
python run.py
```
Send a post to this address
http://127.0.0.1:5000/v1/orders
and this body:
```
{
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
    }
]
}
```