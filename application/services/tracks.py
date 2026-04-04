from domain.interfaces.repositories import ITracksRepository
from domain.entities.track import TrackEntity
from application.services.base import BaseService

class TracksService(BaseService[ITracksRepository, TrackEntity]):
    def __init__(self, tracks_repository: ITracksRepository):
        super().__init__(tracks_repository)
