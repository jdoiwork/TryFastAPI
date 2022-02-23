

from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from typing import Any

from jose import jwt
from loguru import logger

class TokenService(ABC):
    @abstractmethod
    def create(self, data: dict[Any, Any], expire_delta: timedelta | None = None) -> str:
        ...

    @abstractmethod
    def verify(self, token: str):
        ...

class DummyTokenService(TokenService):
    def __init__(self):
        self.secret_key = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

    def create(self, data: dict[Any, Any], expire_delta: timedelta | None = None) -> str:
        expire = self.to_expire(expire_delta or timedelta(minutes=15))
        token = jwt.encode(data | { "exp": expire }, self.secret_key)
        logger.debug({ 'token': token })
        return token

    def to_expire(self, delta: timedelta) -> datetime:
        return datetime.utcnow() + delta

    def verify(self, token: str):
        try:
            logger.debug({ 'token': token })
            payload = jwt.decode(token, self.secret_key)

            return payload
        except Exception as e:
            logger.error(e)
            raise e
