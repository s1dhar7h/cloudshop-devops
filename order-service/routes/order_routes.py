from flask import Blueprint,jsonify
from services.order_services import OrderService
from utils.response import success_response

#user_bp = Blueprint("user",__name__)

order_bp = Blueprint("order",
                    __name__,
                    url_prefix="/api/v1"
)

@order_bp.route("/")
def home():
    return success_response({
        "service": "order-service",
        "status": "running"
    })

@order_bp.route("/health")
def health():
    return success_response({
        "status": "healthy"
    })

@order_bp.route("/orders")
def orders():
    return success_response(
        OrderService.get_all_orders()
    )
    # return jsonify({
    #     "users": [
    #         {
    #             "ID":1,
    #             "Name":"Sidharth",
    #             "email": "sid@example.com"
    #         },
    #         {
    #             "ID":2,
    #             "Name":"Muraleedharan",
    #             "email": "murli@example.com"
    #         }
    #     ]
    # })