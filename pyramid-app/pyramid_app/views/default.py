from pyramid.view import view_config


@view_config(
    route_name='home',
    renderer='pyramid_app:templates/home.jinja2'
)
def home(request):
    return {'project': 'pyramid-app'}


@view_config(
    route_name='about',
    renderer='pyramid_app:templates/about.jinja2'
)
def about(request):
    return {'message': 'About pyramid.'}
