from aiohttp import web


async def test(request: web.Request):
    return web.json_response({}, status=200)
