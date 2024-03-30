import cherrypy

from src.cherrypy_bootstrap import config
from src.cherrypy_bootstrap.application import controllers


if __name__ == "__main__":
    cherrypy.tree.mount(
        controllers.CherryApp(),
        "/",
        config=config.app_config
    )
