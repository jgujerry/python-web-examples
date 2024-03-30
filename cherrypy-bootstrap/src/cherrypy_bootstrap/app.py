import cherrypy

from utils import render


class CherryApp(object):
    
    @cherrypy.expose
    def index(self):
        return render("index.html")
