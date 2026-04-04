from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from domain.entities.playlist import PlaylistEntity
from application.services.playlists import PlaylistsService
from infrastructure.persistence.mongodb.repositories.playlists import PlaylistRepository
from api.dependencies.playlist_dependency import get_playlist_repository

router = APIRouter(prefix="/playlists", tags=["playlists"])


def get_playlists_service(
    repo: PlaylistRepository = Depends(get_playlist_repository),
) -> PlaylistsService:
    return PlaylistsService(repo)


@router.get("/", response_model=List[PlaylistEntity])
async def list_playlists(service: PlaylistsService = Depends(get_playlists_service)):
    return await service.find(params=None)


@router.get("/{playlist_id}", response_model=PlaylistEntity)
async def get_playlist(playlist_id: str, service: PlaylistsService = Depends(get_playlists_service)):
    playlist = await service.get_by_id(playlist_id)
    if not playlist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Playlist not found")
    return playlist


@router.post("/", response_model=PlaylistEntity, status_code=status.HTTP_201_CREATED)
async def create_playlist(playlist: PlaylistEntity, service: PlaylistsService = Depends(get_playlists_service)):
    return await service.create(playlist)


@router.put("/{playlist_id}", response_model=PlaylistEntity)
async def update_playlist(
    playlist_id: str,
    playlist: PlaylistEntity,
    service: PlaylistsService = Depends(get_playlists_service),
):
    updated = await service.update(playlist_id, playlist)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Playlist not found")
    return updated


@router.delete("/{playlist_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_playlist(playlist_id: str, service: PlaylistsService = Depends(get_playlists_service)):
    deleted = await service.delete(playlist_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Playlist not found")
