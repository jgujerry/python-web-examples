from pyramid.view import view_config


@view_config(
    route_name='home',
    renderer='pyramid_html:templates/home.jinja2'
)
def home(request):
    return {'project': 'pyramid-html'}


@view_config(
    route_name='about',
    renderer='pyramid_html:templates/about.jinja2'
)
def about(request):
    return {'message': 'About pyramid.'}
