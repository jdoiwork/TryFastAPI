# pyright: strict

from fastapi import APIRouter, Depends

from services.users_service import UsersService

from .token import verify_token

router = APIRouter(dependencies=[Depends(verify_token)])

@router.get('/')
def index(service: UsersService = Depends()):
    
    return {
        "users": service.index(),           
    }

