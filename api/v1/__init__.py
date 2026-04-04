from fastapi import APIRouter

from api.v1.users import router as users_router
from api.v1.tracks import router as tracks_router
from api.v1.albums import router as albums_router
from api.v1.artists import router as artists_router
from api.v1.playlists import router as playlists_router
from api.v1.playback_history import router as playback_history_router

api_router = APIRouter()

api_router.include_router(users_router)
api_router.include_router(tracks_router)
api_router.include_router(albums_router)
api_router.include_router(artists_router)
api_router.include_router(playlists_router)
api_router.include_router(playback_history_router)
