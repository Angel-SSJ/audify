from domain.interfaces.repositories import IArtistsRepository
from domain.entities.artist import ArtistEntity
from application.services.base import BaseService

class ArtistsService(BaseService[IArtistsRepository, ArtistEntity]):
    def __init__(self, artists_repository: IArtistsRepository):
        super().__init__(artists_repository)
