from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from domain.entities.album import AlbumEntity
from application.services.albums import AlbumsService
from infrastructure.persistence.mongodb.repositories.albums import AlbumsRepository
from api.dependencies.album_dependency import get_album_repository

router = APIRouter(prefix="/albums", tags=["albums"])


def get_albums_service(
    repo: AlbumsRepository = Depends(get_album_repository),
) -> AlbumsService:
    return AlbumsService(repo)


@router.get("/", response_model=List[AlbumEntity])
async def list_albums(service: AlbumsService = Depends(get_albums_service)):
    return await service.find(params=None)


@router.get("/{album_id}", response_model=AlbumEntity)
async def get_album(album_id: str, service: AlbumsService = Depends(get_albums_service)):
    album = await service.get_by_id(album_id)
    if not album:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Album not found")
    return album


@router.post("/", response_model=AlbumEntity, status_code=status.HTTP_201_CREATED)
async def create_album(album: AlbumEntity, service: AlbumsService = Depends(get_albums_service)):
    return await service.create(album)


@router.put("/{album_id}", response_model=AlbumEntity)
async def update_album(
    album_id: str,
    album: AlbumEntity,
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
