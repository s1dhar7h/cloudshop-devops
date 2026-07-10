from utils.logger import logger
class ProductService:

    @staticmethod
    def get_all_products():
        logger.info("Fetching all products")
        return [
            {
                "id":1,
                "name":"Laptop",
                "price": "85000"
            },
            {
                "id":2,
                "Name":"Keyboard",
                "price": "2500"
            }
        ]