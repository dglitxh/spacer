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
from dotenv import load_dotenv

load_dotenv()
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router = APIRouter(prefix="/auth")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def client_user(client_user: schema.ClientUser, user):
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

@router.get("/get_user")
async def get_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=[ALGORITHM])
        email = payload["creds"]
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await models.User.get_or_none(email=email)
    if user is None:
        raise credentials_exception
    client = client_user(client_user, user)
    return client


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
    try:
        hashed_pass = hasher(creds.password)
        creds.password = hashed_pass
        user = await models.User.create(**creds.dict())
        logger.info("User signed up succesfully.")
        token = create_access_token(data={"creds": user.email}, expires_delta=timedelta(30))
        return user
    except Exception as e:
        logger.error("There was an error creating user")
        print(e)



@router.post("/login", summary="Authenticate user")
async def login(creds: schema.Login) -> schema.ClientUser:
    http_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
    try:
        user: schema.ClientUser = await models.User.get_or_none(email=creds.email)
        verify = pwd_context.verify(creds.password, user.password)
        print(verify)
        if not verify:
            raise http_exception
        token = await create_access_token(data={"creds": user.email}, expires_delta=timedelta(minutes=30))
        client = client_user(client_user, user)
        return client
    except Exception as e:
        logger.error("There was an error authenticating this user.")
        print(e)
        raise http_exception
       