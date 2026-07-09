from sqlalchemy.ext.asyncio import (  # type: ignore
    create_async_engine,
    AsyncSession
)

from sqlalchemy.orm import (  # type: ignore
    sessionmaker,
    declarative_base
)

DATABASE_URL = "sqlite+aiosqlite:///./college.db"

engine = create_async_engine(
    DATABASE_URL,
    echo=True
)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session