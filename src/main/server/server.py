from flask import Flask
from flask_cors import CORS
from src.infra.db.settings.connection import db_connection_handler
from src.main.routes.order_routes import order_routes_bp


db_connection_handler.connect_to_db()
app = Flask(__name__)
CORS(app)


app.register_blueprint(order_routes_bp)
