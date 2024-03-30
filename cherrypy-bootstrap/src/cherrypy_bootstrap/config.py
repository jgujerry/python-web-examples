import pathlib

import cherrypy


path = pathlib.Path(__file__).parent.absolute()
app_config = {
  "global" : {
    "server.socket_host" : "127.0.0.1",
    "server.socket_port" : 8080,
    "server.thread_pool" : 8,

    "engine.autoreload.on" : True,

    "tools.trailing_slash.on" : False
  },
  "/static" : {
    "tools.staticdir.on"  : True,
    "tools.staticdir.dir" : path.joinpath("templates")
  }
}

if cherrypy.config.get("environment") == "production":
  app_config["global"]["engine.autoreload.on"] = False
  app_config["global"]["server.thread_pool"] = 30
  app_config["global"]["server.socket_host"] = "0.0.0.0"
  app_config["global"]["server.socket_port"] = 80
  app_config["global"]["environment"] = "production"
  app_config["global"]["log.screen"] = False

else:
  app_config["global"]["environment"] = "development"
  app_config['global']['log.screen'] = True
