# pyright: strict, reportUnusedFunction=false

from fastapi import APIRouter, Depends

from services.users_service import UsersService



router = APIRouter()

@router.get('/')
def index(service: UsersService = Depends()):
    
    return {
        "users": service.index(),           
    }

