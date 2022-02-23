# pyright: strict


from abc import ABC, abstractmethod

class UsersService(ABC):
    @abstractmethod
    def index(self) -> list[dict[str, str]]:
        ...

class DummyUsersService(UsersService):
    def __init__(self):
        pass

    def index(self):
        return [
            { "name": "jdoi-1" },
            { "name": "jdoi-2" },
            { "name": "jdoi-3" },
        ]
