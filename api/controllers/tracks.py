from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from application.services.tracks import TracksService
from api.dependencies.track_dependency import get_tracks_service
from api.helpers.query_params import QueryParams
from api.dtos.tracks import CreateTrackDTO, UpdateTrackDTO, TrackResponse
from typing import Optional

router = APIRouter(prefix="/tracks", tags=["tracks"])



@router.post("/find/", response_model=List[TrackResponse],status_code=status.HTTP_200_OK)
async def get_tracks(service: TracksService = Depends(get_tracks_service), params: QueryParams = None):
    return await service.find(params=params)


@router.get("/{track_id}", response_model=Optional[TrackResponse],status_code=status.HTTP_200_OK)
async def get_track(track_id: str, service: TracksService = Depends(get_tracks_service)):
    return await service.get_by_id(track_id)


@router.post("/", response_model=TrackResponse, status_code=status.HTTP_201_CREATED)
async def create_track(track: CreateTrackDTO, service: TracksService = Depends(get_tracks_service)):
    return await service.create(track)


@router.patch("/{track_id}", response_model=TrackResponse,status_code=status.HTTP_200_OK)
async def update_track(
    track_id: str,
    track: UpdateTrackDTO,
    service: TracksService = Depends(get_tracks_service),
):
    return await service.update(track_id, track)

@router.delete("/{track_id}", status_code=status.HTTP_200_OK)
async def delete_track(track_id: str, service: TracksService = Depends(get_tracks_service)):
    return await service.delete(track_id)

@router.patch("/{track_id}/restore",status_code=status.HTTP_200_OK)
async def restore_track(track_id: str, service: TracksService = Depends(get_tracks_service)):
    return await service.restore(track_id)
