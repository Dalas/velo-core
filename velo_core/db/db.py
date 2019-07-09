from asyncpgsa import create_pool
from asyncpg.pool import Pool
from aiohttp import web


class DBWrapper:
    
    _pool: Pool

    def __init__(self, connection_string):
        self._pool = create_pool(
            dsn=connection_string,
            min_size=5,
            max_size=15
        )

    async def initialize(self):
        await self._pool

    async def fetch(self, query):
        async with self._pool.acquire() as conn:
            return await conn.fetch(query)

    async def fetchrow(self, query):
        async with self._pool.acquire() as conn:
            return await conn.fetchrow(query)

    async def fetchval(self, query):
        async with self._pool.acquire() as conn:
            return await conn.fetchval(query)

    async def acquire(self, query):
        return self._pool.acquire()

    # async def transaction(self):
    #     return self._pool.transaction()

    async def close(self):
        await self._pool.close()


async def setup_connection_pool(app: web.Application):
    app['DB'] = DBWrapper(app['SETTINGS']['db']['cs'])
    await app['DB'].initialize()


async def teardown_connection_pool(app: web.Application):
    await  app['DB'].close()
