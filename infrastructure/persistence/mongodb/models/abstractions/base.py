from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import TypeVar, Generic

T = TypeVar('T')

class BaseModelMongo(BaseModel, Generic[T]):
    id: T = Field(alias="_id")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime | None = None
    deleted_at: datetime | None = None
    is_active: bool = True

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True
    )
