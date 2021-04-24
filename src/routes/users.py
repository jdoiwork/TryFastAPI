# pyright: strict, reportUnusedFunction=false

from fastapi import APIRouter

from services import UsersService
from ioc import Resolver


def create(resolve: Resolver):
    router = APIRouter()

    @router.get('/')
    def index(s: UsersService = resolve(UsersService)):
        
        return {
            "users": s.index(),           
        }

    return router
