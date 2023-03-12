from enum import Enum
from pydantic import BaseModel, EmailStr, ValidationError, Field
import datetime

class UserType(str, Enum):
    SELLER: "seller"
    ADMIN: "admin"
    CUSTOMER: "customer"
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
    cash_total: float

class Product (BaseModel):
    id: int
    name: str
    description: str
    category: str
    quantity: int
    price: float
    rating: float
    
