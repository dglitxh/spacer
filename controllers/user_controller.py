import os
import json
from models import models, schema
from passlib.context import CryptContext
from common.logger import logger
from datetime import datetime, timedelta
from fastapi import Depends, FastAPI, HTTPException, APIRouter, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from common.db import rdb
from controllers.tasks import send_mail
from dotenv import load_dotenv

load_dotenv()
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router = APIRouter(prefix="/auth")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def client_user(client_user: schema.ClientUser, user):
    client_user.id = user.id
    client_user.firstname = user.firstname
    client_user.lastname = user.lastname
    client_user.age = user.age
    client_user.gender = user.gender
    client_user.email = user.email
    client_user.user_type = user.user_type
    return client_user


def hasher(password: str) -> str:
    hashed = pwd_context.hash(password)
    return hashed

credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

def verify_jwt(token) -> dict:
    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=[ALGORITHM])
        email = payload["creds"]
        if email is None:
            raise credentials_exception
            return {
                "vfy": False,
                "email": email
            }
        return {
                "vfy": True,
                "email": email
            }
    except JWTError:
        logger.error(JWTError)
        raise credentials_exception
        return False


@router.get("/get_user")
async def get_user(token: str = Depends(oauth2_scheme)):
    verify = verify_jwt(token)
    if verify["vfy"]:
        email =  verify["email"]
        user = await models.User.get_or_none(email=email)
        if user is None:
            raise credentials_exception
        client = client_user(client_user, user)
        return client
    else: raise credentials_exception

async def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv("SECRET_KEY"), algorithm=ALGORITHM)
    cache_token = await rdb.set("token", encoded_jwt)
    logger.info(encoded_jwt)
    return encoded_jwt


@router.post("/signup", summary="Create an account")
async def signup(creds: schema.User) -> schema.User:
    http_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to create new user!",
                headers={"WWW-Authenticate": "Bearer"},
            )
    try:
        hashed_pass = hasher(creds.password)
        creds.password = hashed_pass
        user = await models.User.create(**creds.dict())
        logger.info("User signed up succesfully.")
        token = await create_access_token(data={"creds": user.email}, expires_delta=timedelta(30))
        client = client_user(client_user, user)
        return client
    except Exception as e:
        logger.error(e)
        raise http_exception



@router.post("/login", summary="Authenticate user")
async def login(creds: schema.Login) -> schema.ClientUser:
    http_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
    try:
        user = await models.User.get_or_none(email=creds.email)
        verify = pwd_context.verify(creds.password, user.password)
        if not verify:
            raise http_exception
        token = await create_access_token(data={"creds": user.email}, expires_delta=timedelta(minutes=30))
        client = client_user(client_user, user)
        return client
    except Exception as e:
        logger.error(e)
        raise http_exception
       
@router.post("/forgot", summary="Authenticate user")
async def forgot_pwd(email: str):
    
    http_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="failed to send reset link",
                headers={"WWW-Authenticate": "Bearer"},
            )
    try:
        user = await models.User.get_or_none(email=creds.email)
        if not user:
            raise http_exception
        token = await create_access_token(data={"creds": user.email}, expires_delta=timedelta(minutes=5))
        template = f"\
        <html>\
            <body>\
                <p>Hi !!!\
                    <br>Click the link below to change your spacer account password</p>\
                <button>\
                    <a href=home/auth/upd_pass/{token}>Reset password</a>\
                </button>\
            </body>\
        </html>\
        "
        send_mail.delay(template, email)
    except Exception as e:
        logger.error(e)
        raise http_exception


@router.put("/upd_pass/{email}", summary="Authenticate user")
async def update(password: str, email: str) -> schema.ClientUser:
    http_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to update password",
                headers={"WWW-Authenticate": "Bearer"},
            )
    try:
        user = await models.User.get_or_none(email=email)
        if not user:
            raise http_exception
        new_pass = hasher(password)
        user.password = new_pass
        await user.update_from_dict(dict(user), exclude_unset=True)
        user.save()
        logger.info("Password update was succesful.")
    except Exception as e:
        logger.error(e)
        raise http_exception   