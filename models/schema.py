from enum import Enum
from pydantic import BaseModel, EmailStr, ValidationError, Field
import datetime

class UserType(str, Enum):
	STANDARD: "standard"
	ORGANIZER: "organizer"
	ADMIN: "admin"

class Gender(str, Enum):
	MALE: "male"
	FEMALE: "female"

class User (BaseModel):
    id: int
    firstname: str
    lastname: str
    age: int
    email: EmailStr
    gender: str
    password: str
    user_type: str

    class Config:
        orm_mode: True

class ClientUser (BaseModel):
    id: int
    firstname: str
    lastname: str
    age: int
    email: EmailStr
    gender: str
    user_type: str

class Login (BaseModel):
    email: EmailStr
    password: str


