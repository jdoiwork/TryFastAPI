


from typing import Protocol
from loguru import logger
from pydantic import BaseSettings
from secrets import token_hex

class SecretService(Protocol):
    @property
    def key(self) -> str:
        ...


class DockerSecrets(BaseSettings):
    token_secret_key: str

    class Config:
        secrets_dir = '/run/secrets'

class DummySecretService(SecretService):
    def __init__(self):
        try:
            ds = DockerSecrets()
            self._key = ds.token_secret_key
            logger.debug("read key from docker secrets.")
        except Exception:    
            logger.debug("use dummy key.")
            self._key = token_hex(32)

    @property
    def key(self) -> str:
        return self._key
