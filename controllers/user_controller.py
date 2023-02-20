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
from common.mailer import send_mail
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

def verify_jwt(token):
    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=[ALGORITHM])
        email = payload["creds"]
        if email is None:
            raise credentials_exception
            return False
        return True
    except JWTError:
        raise credentials_exception
        return False


@router.get("/get_user")
async def get_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    verify_jwt(token)
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
        token = create_access_token(data={"creds": user.email}, expires_delta=timedelta(30))
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
async def forgot_pwd(creds: schema.Login):
    template = """ <html>
        <body>
         
 
        <p>Hi !!!
        <br>Click the link below to change your spacer account password</p>

         <a href"">Reset password</a>
 
        </body>
        </html>
        """
    http_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
    try:
        user = await models.User.get_or_none(email=creds.email)
        if not user:
            raise http_exception
        send_mail(template)
    except Exception as e:
        logger.error(e)
        raise http_exception


@router.put("/upd_pass/{email}", summary="Authenticate user")
async def update(password: str) -> schema.ClientUser:
    http_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
    try:
        user = await models.User.get_or_none(email=query.email)
        if not user:
            raise http_exception
        new_pass = hasher(password)
        user.password = new_pass
        await models.User.update_from_dict(**dict(user))
    except Exception as e:
        logger.error(e)
        raise http_exception