from aiohttp import web

from .app import get_app


def main():
    app = get_app()
    web.run_app(app, port=8080)
