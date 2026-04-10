from domain.interfaces.repositories import IAlbumsRepository
from domain.entities.album import AlbumEntity
from application.services.base import BaseService
from api.dtos.albums import CreateAlbumDTO

class AlbumsService(BaseService[IAlbumsRepository, AlbumEntity]):
    def __init__(self, albums_repository: IAlbumsRepository):
        super().__init__(albums_repository, "Album")
