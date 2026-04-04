from typing import TypeVar, Generic, List, Dict, Optional
from pydantic import BaseModel, Field
from fastapi import Query
from .query_params import QueryParams, SortOrder, FieldFilter

T = TypeVar("T")

class PaginationResult(BaseModel, Generic[T]):
    items: List[T]
    total: int
    offset: int
    limit: int

    @property
    def has_more(self)-> bool:
        return (self.offset + self.limit) < self.total

class PaginationDep:
    def __init__(
        self,
        limit:      int           = Query(default=10, ge=1,  le=500, description="Documentos por página"),
        offset:     int           = Query(default=0,  ge=0,           description="Documentos a saltar"),
        sort_by:    Optional[str] = Query(default=None,                description="Campo por el que ordenar"),
        sort_order: SortOrder     = Query(default=SortOrder.ASC,       description="asc | desc"),
    ):
        self.limit      = limit
        self.offset     = offset
        self.sort_by    = sort_by
        self.sort_order = sort_order

    def to_query_params(
        self,
        filters: Dict[str, FieldFilter] = {},
    ) -> QueryParams:
        return QueryParams(
            filters=filters,
            limit=self.limit,
            offset=self.offset,
            sort_by=self.sort_by,
            sort_order=self.sort_order,
        )
