from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from domain.entities.track import TrackEntity
from application.services.tracks import TracksService
from infrastructure.persistence.mongodb.repositories.tracks import TrackRepository
from api.dependencies.track_dependency import get_track_repository

router = APIRouter(prefix="/tracks", tags=["tracks"])


def get_tracks_service(
    repo: TrackRepository = Depends(get_track_repository),
) -> TracksService:
    return TracksService(repo)


@router.get("/", response_model=List[TrackEntity])
async def list_tracks(service: TracksService = Depends(get_tracks_service)):
    return await service.find(params=None)


@router.get("/{track_id}", response_model=TrackEntity)
async def get_track(track_id: str, service: TracksService = Depends(get_tracks_service)):
    track = await service.get_by_id(track_id)
    if not track:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Track not found")
    return track


@router.post("/", response_model=TrackEntity, status_code=status.HTTP_201_CREATED)
async def create_track(track: TrackEntity, service: TracksService = Depends(get_tracks_service)):
    return await service.create(track)


@router.put("/{track_id}", response_model=TrackEntity)
async def update_track(
    track_id: str,
    track: TrackEntity,
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
