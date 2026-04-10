from contextlib import asynccontextmanager
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from infrastructure.persistence.postgres.postgres import engine
from infrastructure.persistence.mongodb.mongo import db, get_mongo_db
from api.config import settings
from api.controllers import api_router
from domain.exceptions.base import DomainException
from fastapi.responses import JSONResponse


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

@app.exception_handler(DomainException)
async def domain_exception_handler(request, exc: DomainException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.message},
    )

app.include_router(api_router, prefix="/api")
