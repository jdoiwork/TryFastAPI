# pyright: strict


from abc import ABC, abstractmethod

class AdminService(ABC):
    @abstractmethod
    def login(self, user: str, password: str) -> bool:
        ...

class DummyAdminService(AdminService):
    def __init__(self):
        pass

    def login(self, user: str, password: str) -> bool:
        return (
            user == "jdoi" and
            password == "jdoi"
        )
