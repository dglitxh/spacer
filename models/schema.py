from enum import Enum
from pydantic import BaseModel, EmailStr, ValidationError

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
    gender: Gender
    password: str
    user_type: UserType

    class Config:
        orm_mode: True


class TicketType(str, Enum):
    REGULAR: "regular"
    VIP: "vip"

class Ticket(BaseModel):
    id: str
    event_id: str
    user_id: int
    created_at: Field(default_factory=datetime.now())
    ticket_type: TicketType

    class Config:
        orm_mode = True

class TicketPrice(BaseModel):
    regular: float
    vip: float
class Event(BaseModel):
    id: str
    user_id: int
    created_at: Field(default_factory=datetime.now())
    price: TicketPrice
    
    class Config:
        orm_mode = True
