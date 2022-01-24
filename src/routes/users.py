# pyright: strict, reportUnusedFunction=false

from fastapi import APIRouter

from services import UsersService
from ioc import di



router = APIRouter()

@router.get('/')
def index(s: UsersService = di(UsersService)):
    
    return {
        "users": s.index(),           
    }

