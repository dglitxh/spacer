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

class Login (BaseModel):
    email: EmailStr
    password: str

class TicketType(str, Enum):
    REGULAR: "regular"
    VIP: "vip"

class Ticket(BaseModel):
    id: str
    event_id: int
    user_id: int
    ticket_type: str

    class Config:
        orm_mode = True

class TicketPrice(BaseModel):
    regular: float
    vip: float
class Event(BaseModel):
    id: str
    user_id: int
    created_at: str
    price: TicketPrice
    event_date: str
    
    class Config:
        orm_mode = True
