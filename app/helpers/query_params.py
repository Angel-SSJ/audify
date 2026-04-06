from enum import Enum
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class SortOrder(str, Enum):
    ASC  = "asc"
    DESC = "desc"


class FieldFilter(BaseModel):
    eq:       Optional[Any]       = None  # ==
    ne:       Optional[Any]       = None  # !=
    gt:       Optional[Any]       = None  # >
    gte:      Optional[Any]       = None  # >=
    lt:       Optional[Any]       = None  # <
    lte:      Optional[Any]       = None  # <=
    in_:      Optional[List[Any]] = None  # $in
    nin:      Optional[List[Any]] = None  # $nin
    contains: Optional[str]       = None  # $regex case-insensitive
    exists:   Optional[bool]      = None  # $exists


class QueryParams(BaseModel):
    filters:    Dict[str, FieldFilter] = Field(default_factory=dict)
    limit:      int                    = Field(default=10, ge=1, le=500)
    offset:     int                    = Field(default=0, ge=0)
    sort_by:    Optional[str]          = None
    sort_order: SortOrder              = SortOrder.ASC
