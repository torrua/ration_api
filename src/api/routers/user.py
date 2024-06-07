from fastapi import APIRouter

# TODO DRAFT as we have user's router in auth module

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_users():
    return [{"username": "Hiker2000"}, {"username": "Admin2000"}]  # TODO


@router.get("/me")
async def read_user_me():
    return {"username": "Hiker2000"}  # TODO


@router.get("/{username}")
async def read_user(username: str):
    return {"username": username}  # TODO
