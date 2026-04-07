from fastapi import APIRouter

from api.controllers.users import router as users_router
from api.controllers.tracks import router as tracks_router
from api.controllers.albums import router as albums_router
from api.controllers.artists import router as artists_router
from api.controllers.playlists import router as playlists_router
from api.controllers.playback_history import router as playback_history_router
from api.controllers.auth import router as auth_router


api_router = APIRouter()

api_router.include_router(users_router)
api_router.include_router(tracks_router)
api_router.include_router(albums_router)
api_router.include_router(artists_router)
api_router.include_router(playlists_router)
api_router.include_router(playback_history_router)
api_router.include_router(auth_router)
