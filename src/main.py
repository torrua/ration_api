from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .auth.auth import auth_backend
from .auth.base_config import fastapi_users
from .auth.schemas import UserRead, UserCreate
from .api.routers import user


app = FastAPI(title="HikeFuel")


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

origins = [
    "http://localhost:3000",
]

app.include_router(user.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)


@app.get("/")
async def hello():
    return 200, "Ok"