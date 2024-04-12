from .base import *

config = {
  # Global configuration
  'global' : {
    'server.socket_host' : '127.0.0.1',
    'server.socket_port' : 8080,
    'server.thread_pool' : 8,
    'log.screen': True,
    # 'log.access_file': './logs/access.log',
    # 'log.error_file': './logs/error.log',
    
    # Engine
    'engine.autoreload.on' : True,
    
    # Static files
    'tools.staticdir.root': STATIC_ROOTDIR,
    'tools.trailing_slash.on' : False,
    
    # Session
    'tools.sessions.on': True,
    'tools.sessions.storage_type': 'file',
    'tools.sessions.storage_path': './sessions',
    'tools.sessions.timeout': 60,
    
  },

  # Application configuration
  '/static' : {
      'tools.staticdir.on'  : True,
      'tools.staticdir.content_types': {
            'jpg': 'image/jpeg',
            'png': 'image/png',
            'gif': 'image/gif',
            'css': 'text/css',
            'js': 'application/javascript',
        },
    }
}
