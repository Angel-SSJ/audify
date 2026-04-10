from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from application.services.playlists import PlaylistsService
from api.helpers.query_params import QueryParams
from api.dtos.playlist import CreatePlaylistDTO, UpdatePlaylistDTO, PlaylistResponse
from api.dependencies.playlist_dependency import get_playlists_service


router = APIRouter(prefix="/playlists", tags=["playlists"])



@router.post("/find/", response_model=List[PlaylistResponse],status_code=status.HTTP_200_OK)
async def get_playlists(service: PlaylistsService = Depends(get_playlists_service), params: QueryParams = None):
    return await service.find(params=params)


@router.get("/{playlist_id}", response_model=PlaylistResponse,status_code=status.HTTP_200_OK)
async def get_playlist(playlist_id: str, service: PlaylistsService = Depends(get_playlists_service)):
    return await service.get_by_id(playlist_id)


@router.post("/", response_model=PlaylistResponse, status_code=status.HTTP_201_CREATED)
async def create_playlist(playlist: CreatePlaylistDTO, service: PlaylistsService = Depends(get_playlists_service)):
    return await service.create(playlist)


@router.patch("/{playlist_id}", response_model=PlaylistResponse,status_code=status.HTTP_200_OK)
async def update_playlist(
    playlist_id: str,
    playlist: Optional[UpdatePlaylistDTO],
    service: PlaylistsService = Depends(get_playlists_service),
):
    return await service.update(playlist_id, playlist)



@router.delete("/{playlist_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_playlist(playlist_id: str, service: PlaylistsService = Depends(get_playlists_service)):
    return await service.delete(playlist_id)

@router.patch("/{playlist_id}/restore", status_code=status.HTTP_200_OK)
async def restore_playlist(playlist_id: str, service: PlaylistsService = Depends(get_playlists_service)):
    return await service.restore(playlist_id)
