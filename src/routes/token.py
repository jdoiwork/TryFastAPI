# pyright: strict

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

router = APIRouter()

@router.post('/token')
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    
    return {
        "access_token": "token",
        "token_type": "bearer",           
    }

