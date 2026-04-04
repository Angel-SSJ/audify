from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from domain.entities.playback_history import PlaybackHistoryEntity
from application.services.playback_history import PlaybackHistoryService
from infrastructure.persistence.mongodb.repositories.playbacks_history import PlaybackHistoryRepository
from api.dependencies.playback_history_dependency import get_playback_history_repository

router = APIRouter(prefix="/playback-history", tags=["playback-history"])


def get_playback_history_service(
    repo: PlaybackHistoryRepository = Depends(get_playback_history_repository),
) -> PlaybackHistoryService:
    return PlaybackHistoryService(repo)


@router.get("/", response_model=List[PlaybackHistoryEntity])
async def list_history(service: PlaybackHistoryService = Depends(get_playback_history_service)):
    return await service.find(params=None)


@router.get("/{history_id}", response_model=PlaybackHistoryEntity)
async def get_history(history_id: str, service: PlaybackHistoryService = Depends(get_playback_history_service)):
    history = await service.get_by_id(history_id)
    if not history:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="History entry not found")
    return history


@router.post("/", response_model=PlaybackHistoryEntity, status_code=status.HTTP_201_CREATED)
async def create_history(history: PlaybackHistoryEntity, service: PlaybackHistoryService = Depends(get_playback_history_service)):
    return await service.create(history)


@router.put("/{history_id}", response_model=PlaybackHistoryEntity)
async def update_history(
    history_id: str,
    history: PlaybackHistoryEntity,
    service: PlaybackHistoryService = Depends(get_playback_history_service),
):
    updated = await service.update(history_id, history)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="History entry not found")
    return updated


@router.delete("/{history_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_history(history_id: str, service: PlaybackHistoryService = Depends(get_playback_history_service)):
    deleted = await service.delete(history_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="History entry not found")
