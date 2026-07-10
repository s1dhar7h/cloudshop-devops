from flask import Blueprint,jsonify
from services.product_services import ProductService
from utils.response import success_response

#user_bp = Blueprint("user",__name__)

product_bp = Blueprint("product",
                    __name__,
                    url_prefix="/api/v1"
)

@product_bp.route("/")
def home():
    return success_response({
        "service": "product-service",
        "status": "running"
    })

@product_bp.route("/health")
def health():
    return success_response({
        "status": "healthy"
    })

@product_bp.route("/products")
def products():
    return success_response(
        ProductService.get_all_products()
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