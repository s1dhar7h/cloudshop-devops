import requests

from config import Config
from database.db import get_connection
from utils.logger import logger


class OrderService:

    @staticmethod
    def get_all_orders():

        logger.info("Fetching all orders")

        try:
            # Connect to PostgreSQL
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT id, user_id, product_id, status
                FROM orders
            """)

            rows = cursor.fetchall()

            orders = [
                {
                    "id": row[0],
                    "user_id": row[1],
                    "product_id": row[2],
                    "status": row[3]
                }
                for row in rows
            ]

            cursor.close()
            conn.close()

            # Call User Service
            user_response = requests.get(
                f"{Config.USER_SERVICE_URL}/api/v1/users",
                timeout=5
            )

            # Call Product Service
            product_response = requests.get(
                f"{Config.PRODUCT_SERVICE_URL}/api/v1/products",
                timeout=5
            )

            return {
                "orders": orders,
                "users": user_response.json()["data"],
                "products": product_response.json()["data"]
            }

        except requests.exceptions.RequestException as e:
            logger.error(f"Service communication failed: {str(e)}")

            return {
                "error": "Unable to communicate with other services"
            }

        except Exception as e:
            logger.error(f"Database error: {str(e)}")

            return {
                "error": "Unable to fetch orders from database"
            }