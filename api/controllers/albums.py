from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from application.services.albums import AlbumsService
from api.dtos.albums import CreateAlbumDTO, UpdateAlbumDTO, AlbumResponse
from api.helpers.query_params import QueryParams
from api.dependencies.album_dependency import get_albums_service


router = APIRouter(prefix="/albums", tags=["albums"])


@router.post("/find/", response_model=List[AlbumResponse])
async def get_albums(service: AlbumsService = Depends(get_albums_service), params: QueryParams = None):
    return await service.find(params=params)


@router.get("/{album_id}", response_model=AlbumResponse)
async def get_album(album_id: str, service: AlbumsService = Depends(get_albums_service)):
    album = await service.get_by_id(album_id)
    if not album:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Album not found")
    return album


@router.post("/", response_model=AlbumResponse, status_code=status.HTTP_201_CREATED)
async def create_album(album: CreateAlbumDTO, service: AlbumsService = Depends(get_albums_service)):
    return await service.create(album)


@router.put("/{album_id}", response_model=AlbumResponse)
async def update_album(
    album_id: str,
    album: Optional[UpdateAlbumDTO],
    service: AlbumsService = Depends(get_albums_service),
):
    updated = await service.update(album_id, album)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Album not found")
    return updated


@router.delete("/{album_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_album(album_id: str, service: AlbumsService = Depends(get_albums_service)):
    deleted = await service.delete(album_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Album not found")
