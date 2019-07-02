from aiohttp import web

from .router import routes


async def on_startup(app: web.Application):
    pass


async def on_teardown(app: web.Application):
    pass


def get_app():
    app = web.Application()

    app.add_routes(routes)

    return app
