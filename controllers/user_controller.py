from ..models import models, schema
from passlib.context import CryptContext
from ..common.logger import logger
from fastapi import APIRouter

router = APIRouter(prefix="/auth")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hasher(password: str) -> str:
    hashed = pwd_context.hash(password)
    return hashed

@router.post("/signup", summary="Create an account")
async def signup(creds: schema.User) -> schema.User:
    try:
        hashed_pass = hasher(creds.password)
        creds.password = hashed_pass
        user = await models.User.create(creds)
        logger.info("User signed up succesfully.")
        return user
    except Exception as e:
        logger.error("There was an error creating user")
        print(e)



@router.post("/login", summary="Authenticate user")
async def login(creds: schema.Login) -> schema.User:
    try:
        cred_pass = hasher(creds.password)
        user = models.User.get_or_none(email=creds.email)
        return user if user.password == cred_pass else None
    except Exception as e:
        logger.error("There was an error authenticating this user.")
        print(e)