from utils.logger import logger
class OrderService:

    @staticmethod
    def get_all_orders():
        logger.info("Fetching all orders")
        return [
            {
                "id": 101,
                "user_id": 1,
                "product_id": 2,
                "status": "Delivered"
            }
        ]