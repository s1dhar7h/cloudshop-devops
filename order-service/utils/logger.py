import logging
from config import Config

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s | %(levelname)s | %(name)s | %(message)s" ,
    datefmt = "%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(Config.SERVICE_NAME)