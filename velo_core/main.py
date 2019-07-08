from aiohttp import web
import uvloop

from velo_core.app import get_app


def main():
    app = get_app()
    uvloop.install()
    web.run_app(app, port=8080)


if __name__ == '__main__':
    main()
