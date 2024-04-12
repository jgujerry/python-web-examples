import cherrypy

from cherrypy_bootstrap.config import development
from cherrypy_bootstrap.myapp import controllers


if __name__ == "__main__":
    cherrypy.tree.mount(
        controllers.CherryApp(),
        "/",
        config=development.config
    )
    cherrypy.engine.start()
    cherrypy.engine.block()
