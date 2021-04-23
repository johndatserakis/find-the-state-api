from fastapi_users.authentication import JWTAuthentication
from fastapi_users import FastAPIUsers
from main import app, prefix
from models.user import user_db
from schemas.user import User, UserCreate, UserUpdate, UserDB
from fastapi import APIRouter, Depends, Request, Response

JWT_SECRET = "SECRET"  # Replace with env variable

auth_backends = []

jwt_authentication = JWTAuthentication(secret=JWT_SECRET, lifetime_seconds=3600)

auth_backends.append(jwt_authentication)


def on_after_register(user: UserDB, request: Request):
    print(f"User {user.id} has registered.")


def on_after_forgot_password(user: UserDB, token: str, request: Request):
    print(f"User {user.id} has forgot their password. Reset token: {token}")


def after_verification_request(user: UserDB, token: str, request: Request):
    print(f"Verification requested for user {user.id}. Verification token: {token}")


fastapi_users = FastAPIUsers(
    user_db,
    [jwt_authentication],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)

app.include_router(
    fastapi_users.get_auth_router(jwt_authentication),
    prefix=f"{prefix}/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(on_after_register),
    prefix=f"{prefix}/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_reset_password_router(
        JWT_SECRET, after_forgot_password=on_after_forgot_password
    ),
    prefix=f"{prefix}/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_verify_router(
        JWT_SECRET, after_verification_request=after_verification_request
    ),
    prefix=f"{prefix}/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_users_router(), prefix=f"{prefix}/users", tags=["users"]
)

# router = APIRouter()

# https://frankie567.github.io/fastapi-users/configuration/authentication/jwt/#tip-refresh
@app.post(f"{prefix}/auth/jwt/refresh", tags=["auth"])
async def refresh_jwt(
    response: Response, user=Depends(fastapi_users.get_current_active_user)
):
    return await jwt_authentication.get_login_response(user, response)


# app.include_router(router)
