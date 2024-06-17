from .views import hello_world

def setup_routes(app):
    app.add_route(hello_world, '/')
