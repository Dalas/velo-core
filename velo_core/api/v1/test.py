from aiohttp import web

import sqlalchemy as sa

from velo_core.db.tables import UsersTable, AuthTable


async def test(request: web.Request):
    print(await request.app['DB'].fetch(
        sa.select(AuthTable.c)
    ))
    return web.json_response({}, status=200)
