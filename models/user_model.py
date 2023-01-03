from enum import Enum
from pydantic import BaseModel

class UserType(str, Enum):
	STANDARD: "standard"
	ORGANIZER: "organizer"
	ADMIN: "admin"

class Gender(str, Enum):
	MALE: "male"
	FEMALE: "female"

class User (BaseModel):
	firstname: str
	lastname: str
	age: int
	email: EmailStr
	gender: Gender
	password: str
	user_type: UserType