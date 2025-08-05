import os
from dotenv import load_dotenv
from urllib.parse import urlparse
import redis.asyncio

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")
parsed_url = urlparse(DATABASE_URL)

DB_CONFIG = {
    "database": parsed_url.path[1:],  # Remove leading '/'
    "user": parsed_url.username,
    "password": parsed_url.password,
    "host": parsed_url.hostname,
    "port": parsed_url.port,
}

# Shared asyncpg pool
async_connection_pool = None


async def init_db_pool():
    global async_connection_pool
    if async_connection_pool is None:
        import asyncpg
        async_connection_pool = await asyncpg.create_pool(
            min_size=1,
            max_size=10,
            **DB_CONFIG
        )


async def get_db_connection():
    if async_connection_pool is None:
        raise RuntimeError("DB pool not initialized")
    return await async_connection_pool.acquire()


async def return_db_connection(conn):
    await async_connection_pool.release(conn)


# Redis factory
async def get_redis_client():
    return redis.asyncio.Redis(
        host='localhost',
        port=6379,
        db=0,
        decode_responses=True
    )
