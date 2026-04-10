from typing import List, Optional
from application.services.artists import ArtistsService
from api.helpers.query_params import QueryParams
from api.dtos.artists import CreateArtistDTO, UpdateArtistDTO, ArtistResponse
from api.dependencies.artist_dependency import get_artists_service
from fastapi import APIRouter, Depends, HTTPException, status


router = APIRouter(prefix="/artists", tags=["artists"])


@router.post("/find/", response_model=List[ArtistResponse],status_code=status.HTTP_200_OK)
async def get_artists(service: ArtistsService = Depends(get_artists_service), params: QueryParams = None):
    return await service.find(params=params)


@router.get("/{artist_id}", response_model=ArtistResponse,status_code=status.HTTP_200_OK)
async def get_artist(artist_id: str, service: ArtistsService = Depends(get_artists_service)):
    return await service.get_by_id(artist_id)


@router.post("/", response_model=ArtistResponse, status_code=status.HTTP_201_CREATED)
async def create_artist(artist: CreateArtistDTO, service: ArtistsService = Depends(get_artists_service)):
    return await service.create(artist)


@router.patch("/{artist_id}", response_model=ArtistResponse,status_code=status.HTTP_200_OK)
async def update_artist(
    artist_id: str,
    artist: Optional[UpdateArtistDTO],
    service: ArtistsService = Depends(get_artists_service),
):
    return await service.update(artist_id, artist)


@router.delete("/{artist_id}", status_code=status.HTTP_200_OK)
async def delete_artist(artist_id: str, service: ArtistsService = Depends(get_artists_service)):
    return await service.delete(artist_id)

@router.patch("/{artist_id}/restore", status_code=status.HTTP_200_OK)
async def restore_artist(artist_id: str, service: ArtistsService = Depends(get_artists_service)):
    return await service.restore(artist_id)
