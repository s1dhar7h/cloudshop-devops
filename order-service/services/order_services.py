import requests
from config import Config
from utils.logger import logger

class OrderService:
    @staticmethod
    def get_all_orders():
        
        logger.info("Fetching all orders")
        
        try:
            user_response= requests.get(
                f"{Config.USER_SERVICE_URL}/api/v1/users",
                timeout=5
            )
            product_response= requests.get(
                f"{Config.PRODUCT_SERVICE_URL}/api/v1/products",
                timeout=5
            )        
        
            return {
                "orders": [
                    {
                        "id": 101,
                        "user_id": 1,
                        "product_id": 2,
                        "status": "Delivered"
                    }
                ],
                "users": user_response.json()["data"],
                "products": product_response.json()["data"]
            }

        except requests.exceptions.RequestException as e:
            logger.error(str(e))
            return{
                "error": "Unable to communicate with other services"
            }