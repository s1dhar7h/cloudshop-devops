from database.db import get_connection
from utils.logger import logger


class ProductService:

    @staticmethod
    def get_all_products():

        logger.info("Fetching all products from PostgreSQL")

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, name, price FROM products"
        )

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return [
            {
                "id": row[0],
                "name": row[1],
                "price": float(row[2])
            }
            for row in rows
        ]