
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from services.admin_service import AdminService
from services.token_service import TokenService


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

async def verify_token(access_token: str = Depends(oauth2_scheme), token: TokenService = Depends()):
    token.verify(access_token)

def unauth():
    return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid authentication credentials',
            headers={
                "WWW-Authenticate": "Bearer",
            })

router = APIRouter()

@router.post('/token')
async def login(form_data: OAuth2PasswordRequestForm = Depends(), admin: AdminService = Depends(), token: TokenService = Depends()):
    if admin.login(form_data.username, form_data.password):
        access_token = token.create({ "sub": form_data.username })
        return {
            "access_token": access_token,
            "token_type": "bearer",           
        }
    else:
        raise unauth()

