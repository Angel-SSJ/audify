from typing import TypeVar, Generic, Optional, Any, List
from abc import ABC, abstractmethod
from pydantic import BaseModel
from domain.entities.user import UserEntity
from domain.entities.playlist import PlaylistEntity
from domain.entities.track import TrackEntity
from domain.entities.album import AlbumEntity
from domain.entities.artist import ArtistEntity
from domain.entities.playback_history import PlaybackHistoryEntity

E = TypeVar("E", bound=BaseModel)

class IBaseRepository(ABC, Generic[E]):
    @abstractmethod
    async def create(self, domain_entity: E) -> E:
        pass

    @abstractmethod
    async def get_by_id(self, id: str) -> Optional[E]:
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

class IUsersRepository(IBaseRepository[UserEntity]):
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
