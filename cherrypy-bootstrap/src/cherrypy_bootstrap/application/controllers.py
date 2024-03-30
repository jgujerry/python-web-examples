import cherrypy

from src.cherrypy_bootstrap.utilities import render


class CherryApp(object):
    
    @cherrypy.expose
    def index(self):
        return render("index.html")
