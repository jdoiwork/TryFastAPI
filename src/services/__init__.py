# pyright: strict, reportUnusedImport=false

from services.db_service    import DbService
from services.users_service import UsersService

class Service:
    def __init__(self, db: DbService):
        self.db = db

