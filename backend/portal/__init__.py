import datetime

import arrow
from pyramid.config import Configurator
from pyramid.renderers import JSON

from .api.auth import routes as auth_routes
from .api.public import routes as public_routes


def routes(config):
    auth_routes.make(config)
    public_routes.make(config)


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application. """
    with Configurator(settings=settings) as config:
        config.include(routes)
        config.include(renderers)
        config.scan()
    return config.make_wsgi_app()


def renderers(config):
    json_renderer = JSON()
    json_renderer.add_adapter(arrow.Arrow, lambda obj, request: str(obj))
    json_renderer.add_adapter(datetime.date, lambda obj, request: str(obj))
    config.add_renderer('json', json_renderer)