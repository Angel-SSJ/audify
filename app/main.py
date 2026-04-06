from contextlib import asynccontextmanager
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from infrastructure.persistence.mongodb.mongo import db, get_mongo_db
from app.config import settings
from api.controllers import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    db.client = AsyncIOMotorClient(settings.mongo_connection)
    yield
    db.client.close()


app = FastAPI(
    title="Audify API",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(api_router, prefix="/api")
