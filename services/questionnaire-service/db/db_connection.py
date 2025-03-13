from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("POSTGRES_CONN_STRING")

if not DATABASE_URL.startswith("postgresql+asyncpg://"):
    raise ValueError("❌ ERROR: Database URL must use 'asyncpg'!")

async def get_asyncpg_connection():
    return await asyncpg.connect(DATABASE_URL, ssl="require")

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    future=True,
    connect_args={"ssl": "require"}
)

Base = declarative_base()

# Create async session factory
async_session = sessionmaker(
    bind=engine, 
    expire_on_commit=False, 
    class_=AsyncSession
)

# Dependency for routes to use
async def get_db():
    async with async_session() as session:
        yield session
