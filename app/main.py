from contextlib import asynccontextmanager
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from app.db.mongodb.mongo import db
from app.core.config import settings
from app.controllers import api_router

@asynccontextmanager
async def lifespan(app:FastAPI):

    db.client = AsyncIOMotorClient(settings.mongo_connection)
    yield
    db.client.close()


app = FastAPI(lifespan=lifespan)

app.include_router(api_router,prefix="/api")
