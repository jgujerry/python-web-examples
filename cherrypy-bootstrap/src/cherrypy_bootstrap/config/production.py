from .base import *


config = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 80,
        'server.thread_pool': 100,
        'server.environment': 'production',
        'engine.autoreload.on': False,
        'log.screen': False,
        'log.access_file': '/var/log/cherrypy/access.log',
        'log.error_file': '/var/log/cherrypy/error.log',
        'tools.staticdir.root': STATIC_ROOTDIR,
        'tools.sessions.on': True,
        'tools.sessions.storage_type': 'file',
        'tools.sessions.storage_path': '/var/lib/cherrypy/sessions',
        'tools.sessions.timeout': 3600,
        
        # Templates
        'tools.jinja2.on': True,
        'tools.jinja2.template_dir': TEMPLATE_DIR
    },
    '/static': {
        'tools.staticdir.on': True,
        'tools.staticdir.content_types': {
            'jpg': 'image/jpeg',
            'png': 'image/png',
            'gif': 'image/gif',
            'css': 'text/css',
            'js': 'application/javascript',
        },
    },
}
