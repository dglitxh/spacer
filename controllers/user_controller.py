from models import models, schema
from passlib.context import CryptContext
from common.logger import logger
from datetime import datetime, timedelta
from fastapi import Depends, FastAPI, HTTPException, APIRouter, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from dotenv import load_dotenv

load_dotenv()
ALGORITHM = "HS256"

router = APIRouter(prefix="/auth")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hasher(password: str) -> str:
    hashed = pwd_context.hash(password)
    return hashed

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv("SECRET_KEY"), algorithm=ALGORITHM)
    return encoded_jwt

@router.post("/signup", summary="Create an account")
async def signup(creds: schema.User) -> schema.User:
    try:
        hashed_pass = hasher(creds.password)
        creds.password = hashed_pass
        user = await models.User.create(**creds.dict())
        logger.info("User signed up succesfully.")
        return user
    except Exception as e:
        logger.error("There was an error creating user")
        print(e)



@router.post("/login", summary="Authenticate user")
async def login(creds: schema.Login) -> schema.ClientUser:
    try:
        cred_pass = hasher(creds.password)
        db_user = models.User.get_or_none(email=creds.email)
        verify = pwd_context.verify(cred_pass, user.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return user if verify else None
    except Exception as e:
        logger.error("There was an error authenticating this user.")
        print(e)