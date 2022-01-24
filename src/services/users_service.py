# pyright: strict

from services.db_service import DbService

class UsersService:
    def __init__(self, db: DbService):
        self.db = db

    def index(self):
        # TODO for you: Get from db
        # users = db.select('*').from('users')
        return [
            { "name": "jdoi-1" },
            { "name": "jdoi-2" },
            { "name": "jdoi-3" },
        ]
