from pydantic import BaseModel, Field
from datetime import datetime

class TicketPrice(BaseModel):
    regular: float
    vip: float
class Event(BaseModel):
    id: str
    user_id: int
    created_at: Field(default_factory=datetime.now())
 
