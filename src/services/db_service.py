
from loguru import logger

class DbService:
    def __init__(self) -> None:
        logger.debug(DbService)
        self.name = "sqlite"
