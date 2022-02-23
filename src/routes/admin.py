# pyright: strict

from fastapi import APIRouter, Depends

from services.users_service import UsersService

from .token import oauth2_scheme

router = APIRouter()

@router.get('/')
def index(service: UsersService = Depends(), token: str = Depends(oauth2_scheme)):
    
    return {
        "users": service.index(),           
    }

