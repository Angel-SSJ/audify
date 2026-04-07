from contextlib import asynccontextmanager
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from infrastructure.persistence.postgres.postgres import engine
from infrastructure.persistence.mongodb.mongo import db, get_mongo_db
from api.config import settings
from api.controllers import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    db.client = AsyncIOMotorClient(settings.mongo_connection)
    yield
    db.client.close()
    await engine.dispose()


app = FastAPI(
    title="Audify",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(api_router, prefix="/api")
