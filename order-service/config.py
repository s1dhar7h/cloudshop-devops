import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SERVICE_NAME = os.getenv("SERVICE_NAME", "order-service")
    HOST = os.getenv("HOST","0.0.0.0")
    PORT = int(os.getenv("PORT",5003))
    DEBUG = os.getenv("DEBUG","True").lower() == "true"
    USER_SERVICE_URL = os.getenv(
        "USER_SERVICE_URL",
        "http://user-service:5001"
    )
    PRODUCT_SERVICE_URL = os.getenv(
        "PRODUCT_SERVICE_URL",
        "http://product-service:5001"
    )