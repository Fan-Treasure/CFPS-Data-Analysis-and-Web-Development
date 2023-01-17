from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT


router = APIRouter()

@router.post('/verify')
def verify_token_alive(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

@router.post('/refresh')
def refresh_token(Authorize: AuthJWT = Depends()):
    Authorize.jwt_refresh_token_required()
    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=current_user, fresh=False)
    return {"access_token": new_access_token}