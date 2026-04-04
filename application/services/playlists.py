from domain.interfaces.repositories import IPlaylistsRepository
from domain.entities.playlist import PlaylistEntity
from application.services.base import BaseService

class PlaylistsService(BaseService[IPlaylistsRepository, PlaylistEntity]):
    def __init__(self, playlists_repository: IPlaylistsRepository):
        super().__init__(playlists_repository)
