from typing import TypeVar, Generic
from abc import ABC, abstractmethod
from typing import Protocol
from pydantic import BaseModel

D = TypeVar("D", bound=BaseModel)
P = TypeVar("P", bound=BaseModel)

class IMapper(Protocol[D, P]):
    @abstractmethod
    def to_domain(self, persistence_schema: P) -> D:
        pass

    @abstractmethod
    def to_persistence(self, domain_entity: D) -> P:
        pass
