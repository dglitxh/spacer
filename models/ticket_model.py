from pydantic import BaseModel, Field
from datetime import datetime

class TicketType(str, Enum):
    REGULAR: "regular"
    VIP: "vip"

class Ticket(BaseModel):
    id: str
    event_id: str
    user_id: int
    created_at: Field(default_factory=datetime.now())
    ticket_type: TicketType
