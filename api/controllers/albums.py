from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from application.services.albums import AlbumsService
from api.dtos.albums import CreateAlbumDTO, UpdateAlbumDTO, AlbumResponse
from api.helpers.query_params import QueryParams
from api.dependencies.album_dependency import get_albums_service


router = APIRouter(prefix="/albums", tags=["albums"])


@router.post("/find/", response_model=List[AlbumResponse],status_code=status.HTTP_200_OK)
async def get_albums(service: AlbumsService = Depends(get_albums_service), params: QueryParams = None):
    return await service.find(params=params)


@router.get("/{album_id}", response_model=AlbumResponse,status_code=status.HTTP_200_OK)
async def get_album(album_id: str, service: AlbumsService = Depends(get_albums_service)):
    return await service.get_by_id(album_id)



@router.post("/", response_model=AlbumResponse, status_code=status.HTTP_201_CREATED)
async def create_album(album: CreateAlbumDTO, service: AlbumsService = Depends(get_albums_service)):
    return await service.create(album)


@router.patch("/{album_id}", response_model=AlbumResponse,status_code=status.HTTP_200_OK)
async def update_album(
    album_id: str,
    album: UpdateAlbumDTO,
    service: AlbumsService = Depends(get_albums_service),
):
    return await service.update(album_id, album)


@router.delete("/{album_id}", status_code=status.HTTP_200_OK)
async def delete_album(album_id: str, service: AlbumsService = Depends(get_albums_service)):
    return await service.delete(album_id)


@router.patch("/{album_id}/restore", status_code=status.HTTP_200_OK)
async def restore_album(album_id: str, service: AlbumsService = Depends(get_albums_service)):
    return await service.restore(album_id)
