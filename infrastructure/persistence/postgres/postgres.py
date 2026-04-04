from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.config import settings

engine = create_async_engine(settings.postgres_connection, echo=True, future=True)

AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def get_pg_db():
    async with AsyncSessionLocal() as session:
        yield session
