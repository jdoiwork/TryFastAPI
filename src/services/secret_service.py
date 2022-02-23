


from typing import Protocol


class SecretService(Protocol):
    @property
    def key(self) -> str:
        ...


class DummySecretService(SecretService):
    def __init__(self):
        self._key = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

    @property
    def key(self) -> str:
        return self._key
