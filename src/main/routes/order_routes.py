from flask import Blueprint, jsonify, request
from src.main.adapters.request_adapter import request_adapter
from src.main.composer.order_register_composer import order_register_composer
from src.presentation.error_handler.error_controller import handle_errors
from src.validators.order_register_validator import order_register_validator


order_routes_bp = Blueprint("order_routes", __name__)


@order_routes_bp.route("/v1/orders", methods=["POST"])
def register_order():
    http_response = None

    try:
        order_register_validator(request)
        http_response = request_adapter(request, order_register_composer().handle)
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code
