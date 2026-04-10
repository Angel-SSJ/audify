from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from application.services.playback_history import PlaybackHistoryService
from api.helpers.query_params import QueryParams
from api.dtos.playback_history import CreatePlaybackHistoryDTO, UpdatePlaybackHistoryDTO, PlaybackHistoryResponse
from api.dependencies.playback_history_dependency import get_playback_histories_service

router = APIRouter(prefix="/playback-history", tags=["playback-history"])


@router.post("/find/", response_model=List[PlaybackHistoryResponse],status_code=status.HTTP_200_OK)
async def get_playback_histories(service: PlaybackHistoryService = Depends(get_playback_histories_service), params: QueryParams = None):
    return await service.find(params=params)


@router.get("/{history_id}", response_model=PlaybackHistoryResponse,status_code=status.HTTP_200_OK)
async def get_playback_history(history_id: str, service: PlaybackHistoryService = Depends(get_playback_histories_service)):
    return await service.get_by_id(history_id)


@router.post("/", response_model=PlaybackHistoryResponse, status_code=status.HTTP_201_CREATED)
async def create_playback_history(history: CreatePlaybackHistoryDTO, service: PlaybackHistoryService = Depends(get_playback_histories_service)):
    return await service.create(history)


@router.patch("/{history_id}", response_model=PlaybackHistoryResponse,status_code=status.HTTP_200_OK)
async def update_playback_history(
    history_id: str,
    history: Optional[UpdatePlaybackHistoryDTO],
    service: PlaybackHistoryService = Depends(get_playback_histories_service),
):
    return await service.update(history_id, history)


@router.delete("/{history_id}", status_code=status.HTTP_200_OK)
async def delete_playback_history(history_id: str, service: PlaybackHistoryService = Depends(get_playback_histories_service)):
    return await service.delete(history_id)

@router.patch("/{history_id}/restore", status_code=status.HTTP_200_OK)
async def restore_playback_history(history_id: str, service: PlaybackHistoryService = Depends(get_playback_histories_service)):
    return await service.restore(history_id)
