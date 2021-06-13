from pyramid.view import view_config


@view_config(route_name='sign_up',
             renderer='json')
def sign_in(request):
    return {'test':'test', 'test1':'test1'}
