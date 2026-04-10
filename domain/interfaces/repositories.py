from typing import TypeVar, Generic, Optional, Any, List
from abc import ABC, abstractmethod
from pydantic import BaseModel
from domain.entities.user import UserEntity
from domain.entities.playlist import PlaylistEntity
from domain.entities.track import TrackEntity
from domain.entities.album import AlbumEntity
from domain.entities.artist import ArtistEntity
from domain.entities.playback_history import PlaybackHistoryEntity
from domain.entities.user import UserEntity

E = TypeVar("E", bound=BaseModel)

class IBaseRepository(ABC, Generic[E]):
    @abstractmethod
    async def create(self, domain_entity: E) -> E:
        pass

    @abstractmethod
    async def get_by_id(self, id: str, is_active: bool = True) -> Optional[E]:
        pass

    @abstractmethod
    async def find(self,params:Any)->List[E]:
        pass

    @abstractmethod
    async def update(self, id: str, entity: Optional[E]) -> Optional[E]:
        pass

    @abstractmethod
    async def delete(self, id: str) -> bool:
        pass

    @abstractmethod
    async def restore(self, id: str) -> bool:
        pass

class IUsersRepository(IBaseRepository[UserEntity]):
    @abstractmethod
    async def create(self, domain_entity: UserEntity) -> UserEntity:
        pass
    @abstractmethod
    async def update(self, id: str, entity: Optional[UserEntity]) -> Optional[UserEntity]:
        pass
    @abstractmethod
    async def delete(self, id: str) -> bool:
        pass
    @abstractmethod
    async def get_by_email(self, email: str) -> Optional[UserEntity]:
        pass

    @abstractmethod
    async def valid_password(self, user_id: str, password: str) -> bool:
        pass


class IPlaylistsRepository(IBaseRepository[PlaylistEntity]):
    pass

class ITracksRepository(IBaseRepository[TrackEntity]):
    pass

class IAlbumsRepository(IBaseRepository[AlbumEntity]):
    pass

class IArtistsRepository(IBaseRepository[ArtistEntity]):
    pass

class IPlaybackHistoryRepository(IBaseRepository[PlaybackHistoryEntity]):
    pass

class IBaseRepositoryPostgres(ABC, Generic[E]):

    @abstractmethod
    async def get_by_id(self, id: str) -> Optional[E]:
        pass
    @abstractmethod
    async def create(self, domain_entity: E) -> E:
        pass



    @abstractmethod
    async def update(self, id: str, entity: Optional[E]) -> Optional[E]:
        pass

    @abstractmethod
    async def delete(self, id: str) -> bool:
        pass

class IUsersRepositoryPostgres(IBaseRepositoryPostgres[UserEntity]):
    @abstractmethod
    async def get_by_email(self, email: str) -> Optional[UserEntity]:
        pass
    @abstractmethod
    async def valid_password(self, user_id: str, password: str) -> bool:
        pass



class IRoleRepository(ABC):
    @abstractmethod
    async def get_by_id(self, id: str) -> Optional[RoleEntity]:
        pass

    @abstractmethod
    async def get_by_name(self, name: str) -> Optional[RoleEntity]:
        pass

    @abstractmethod
    async def create(self, role: RoleEntity) -> RoleEntity:
        pass

    @abstractmethod
    async def update(self, id: str, role: RoleEntity) -> RoleEntity:
        pass

    @abstractmethod
    async def delete(self, id: str) -> bool:
        pass

class IRoleUserRepository(ABC):
    @abstractmethod
    async def get_by_id(self, id: str) -> Optional[RoleUserEntity]:
        pass

    @abstractmethod
    async def get_by_user_id(self, user_id: str) -> Optional[RoleUserEntity]:
        pass

    @abstractmethod
    async def get_by_role_id(self, role_id: str) -> Optional[RoleUserEntity]:
        pass

    @abstractmethod
    async def create(self, role_user: RoleUserEntity) -> RoleUserEntity:
        pass

    @abstractmethod
    async def update(self, id: str, role_user: RoleUserEntity) -> RoleUserEntity:
        pass

    @abstractmethod
    async def delete(self, id: str) -> bool:
        pass
