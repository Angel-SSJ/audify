from domain.interfaces.repositories import IPlaybackHistoryRepository
from domain.entities.playback_history import PlaybackHistoryEntity
from application.services.base import BaseService

class PlaybackHistoryService(BaseService[IPlaybackHistoryRepository, PlaybackHistoryEntity]):
    def __init__(self, playback_history_repository: IPlaybackHistoryRepository):
        super().__init__(playback_history_repository, "Playback History")
