from fastapi import APIRouter, Depends

from src.api.models import User as UserORM
from src.api.schemas.user import User
from src.auth.base_config import current_user

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/me")
def read_user_me(user: UserORM = Depends(current_user)):
    return User.model_validate(user)
