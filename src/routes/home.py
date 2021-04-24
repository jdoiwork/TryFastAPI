from typing import Callable
from fastapi import APIRouter
from loguru import logger

from models import Name
from services import Service
from ioc import Resolver


def create(resolve: Resolver):
    router = APIRouter()

    @router.get('/{name}')
    def show(name: Name, s: Service = resolve(Service)):
        logger.info(s.db)
        logger.info(s.db.name)
        return {
            "hello": name,
            "db-name": s.db.name
        }

    return router
