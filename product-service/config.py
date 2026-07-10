import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SERVICE_NAME = "product-service"
    HOST = os.getenv("HOST","0.0.0.0")
    PORT = int(os.getenv("PORT",5002))
    DEBUG = os.getenv("DEBUG","True").lower() == "true"