from aiohttp import web

from .api import v1


routes = [
    web.get('/test', v1.test)
]
