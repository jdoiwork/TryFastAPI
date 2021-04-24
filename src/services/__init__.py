from typing import Callable, Type, TypeVar


class DbService:
    def __init__(self) -> None:
        self.name = "sqlite"

class Service:
    def __init__(self, db: DbService):
        self.db = db


