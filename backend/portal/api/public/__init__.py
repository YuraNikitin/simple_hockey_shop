from pyramid.view import view_config


@view_config(route_name='home',
             request_method='GET',
             renderer='public/home/index.mako')
def contacts(request):
    return {}
