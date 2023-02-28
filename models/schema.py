from enum import Enum
from pydantic import BaseModel, EmailStr, ValidationError, Field
import datetime
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


class Store (BaseModel):
    id: int
    name: str 
    category: str

class Product (BaseModel):
    id: int
    name: str
    category: str
    quantity: int
    price: float
    rating: float
    
