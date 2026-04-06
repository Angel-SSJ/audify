from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from application.services.tracks import TracksService
from api.dependencies.track_dependency import get_tracks_service
from app.helpers.query_params import QueryParams
from api.dtos.tracks import CreateTrackDTO, UpdateTrackDTO, TrackResponse
from typing import Optional

router = APIRouter(prefix="/tracks", tags=["tracks"])



@router.post("/find/", response_model=List[TrackResponse])
async def get_tracks(service: TracksService = Depends(get_tracks_service), params: QueryParams = None):
    return await service.find(params=params)


@router.get("/{track_id}", response_model=TrackResponse)
async def get_track(track_id: str, service: TracksService = Depends(get_tracks_service)):
    track = await service.get_by_id(track_id)
    if not track:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Track not found")
    return track


@router.post("/", response_model=TrackResponse, status_code=status.HTTP_201_CREATED)
async def create_track(track: CreateTrackDTO, service: TracksService = Depends(get_tracks_service)):
    return await service.create(track)


@router.put("/{track_id}", response_model=TrackResponse)
async def update_track(
    track_id: str,
    track: Optional[UpdateTrackDTO],
    service: TracksService = Depends(get_tracks_service),
):
    updated = await service.update(track_id, track)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Track not found")
    return updated


@router.delete("/{track_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_track(track_id: str, service: TracksService = Depends(get_tracks_service)):
    deleted = await service.delete(track_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Track not found")
