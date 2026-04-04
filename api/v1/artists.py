from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from domain.entities.artist import ArtistEntity
from application.services.artists import ArtistsService
from infrastructure.persistence.mongodb.repositories.artists import ArtistRepository
from api.dependencies.artist_dependency import get_artist_repository

router = APIRouter(prefix="/artists", tags=["artists"])


def get_artists_service(
    repo: ArtistRepository = Depends(get_artist_repository),
) -> ArtistsService:
    return ArtistsService(repo)


@router.get("/", response_model=List[ArtistEntity])
async def list_artists(service: ArtistsService = Depends(get_artists_service)):
    return await service.find(params=None)


@router.get("/{artist_id}", response_model=ArtistEntity)
async def get_artist(artist_id: str, service: ArtistsService = Depends(get_artists_service)):
    artist = await service.get_by_id(artist_id)
    if not artist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Artist not found")
    return artist


@router.post("/", response_model=ArtistEntity, status_code=status.HTTP_201_CREATED)
async def create_artist(artist: ArtistEntity, service: ArtistsService = Depends(get_artists_service)):
    return await service.create(artist)


@router.put("/{artist_id}", response_model=ArtistEntity)
async def update_artist(
    artist_id: str,
    artist: ArtistEntity,
    service: ArtistsService = Depends(get_artists_service),
):
    updated = await service.update(artist_id, artist)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Artist not found")
    return updated


@router.delete("/{artist_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_artist(artist_id: str, service: ArtistsService = Depends(get_artists_service)):
    deleted = await service.delete(artist_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Artist not found")
