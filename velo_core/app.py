from aiohttp import web

from .db import setup_connection_pool, teardown_connection_pool
from .router import routes
from .settings import load_settings


async def on_startup(app: web.Application):
    await setup_connection_pool(app)


async def on_teardown(app: web.Application):
    await teardown_connection_pool(app)


def get_app():
    app = web.Application()

    app['SETTINGS'] = load_settings()
    app.add_routes(routes)

    return app
