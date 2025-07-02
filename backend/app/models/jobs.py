from pydantic import BaseModel
from typing import Optional

class Job(BaseModel):
    id: Optional[int] = None
    company: str
    role: str
    status: str  # e.g., "Applied", "Interview", "Rejected", "Offer"
    