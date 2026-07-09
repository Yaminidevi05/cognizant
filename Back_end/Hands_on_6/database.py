try:
    # import dynamically to avoid static analysis/import-time issues in editors
    import importlib

    _asyncio_mod = importlib.import_module("sqlalchemy.ext.asyncio")
    create_async_engine = getattr(_asyncio_mod, "create_async_engine")
    AsyncSession = getattr(_asyncio_mod, "AsyncSession")
    
    _orm_mod = importlib.import_module("sqlalchemy.orm")
    sessionmaker = getattr(_orm_mod, "sessionmaker")
    declarative_base = getattr(_orm_mod, "declarative_base")
except Exception as e:  # ImportError or ModuleNotFoundError
    raise ImportError(
        "sqlalchemy.ext.asyncio or sqlalchemy.orm could not be imported.\n"
        "Make sure SQLAlchemy>=1.4 and the async extras are installed, e.g.:\n"
        "pip install 'sqlalchemy[asyncio]' aiosqlite"
    ) from e

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