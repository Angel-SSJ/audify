from pydantic import BaseModel
from typing import Optional

class BaseEntity(BaseModel):
    id: Optional[str] = None
    is_active: bool = True
