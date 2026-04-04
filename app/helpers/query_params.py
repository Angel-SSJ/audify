from enum import Enum
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class SortOrder(str, Enum):
    ASC  = "asc"
    DESC = "desc"


class FieldFilter(BaseModel):
    """
    Operadores disponibles para filtrar un campo.
 
    Ejemplos:
        FieldFilter(eq="active")
        FieldFilter(gte=18, lte=65)
        FieldFilter(in_=["admin", "user"])
        FieldFilter(contains="john")
    """
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
    """
    Parámetros de consulta genéricos para cualquier colección.
    Cada clave en `filters` corresponde a un campo de la entidad.
 
    Ejemplo:
        QueryParams(
            filters={
                "status": FieldFilter(eq="active"),
                "age":    FieldFilter(gte=18, lte=65),
                "role":   FieldFilter(in_=["admin", "editor"]),
                "name":   FieldFilter(contains="john"),
            },
            limit=20,
            offset=0,
            sort_by="created_at",
            sort_order=SortOrder.DESC,
        )
    """
    filters:    Dict[str, FieldFilter] = Field(default_factory=dict)
    limit:      int                    = Field(default=10, ge=1, le=500)
    offset:     int                    = Field(default=0, ge=0)
    sort_by:    Optional[str]          = None
    sort_order: SortOrder              = SortOrder.ASC
