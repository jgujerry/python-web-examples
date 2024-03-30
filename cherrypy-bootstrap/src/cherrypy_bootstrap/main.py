import cherrypy

from app import CherryApp


if __name__ == "__main__":
    cherrypy.quickstart(CherryApp())
