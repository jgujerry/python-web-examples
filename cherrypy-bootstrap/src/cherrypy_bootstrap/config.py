import pathlib

import cherrypy


path = pathlib.Path(__file__).parent.absolute()


app_config = {
  "/": {
        "tools.sessions.on": True,
        "tools.staticdir.root": "/path/to/static/files",
    },
  "/static" : {
      "tools.staticdir.on"  : True,
      "tools.staticdir.dir" : path.joinpath("templates")
  }
}

global_config = {
  "global" : {
    "server.socket_host" : "127.0.0.1",
    "server.socket_port" : 8080,
    "server.thread_pool" : 8,

    "engine.autoreload.on" : True,

    "tools.trailing_slash.on" : False
  },
  
}

if cherrypy.config.get("environment") == "production":
  global_config["global"]["engine.autoreload.on"] = False
  global_config["global"]["server.thread_pool"] = 30
  global_config["global"]["server.socket_host"] = "0.0.0.0"
  global_config["global"]["server.socket_port"] = 80
  global_config["global"]["environment"] = "production"
  global_config["global"]["log.screen"] = False

else:
  global_config["global"]["environment"] = "development"
  global_config['global']['log.screen'] = True
