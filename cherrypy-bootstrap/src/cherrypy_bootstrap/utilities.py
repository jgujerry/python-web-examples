import cherrypy
from jinja2 import Environment, FileSystemLoader
from cherrypy_bootstrap.config.base import TEMPLATE_DIR

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))


def render(template_name, **kwargs):
    template = env.get_template(template_name)
    return template.render(**kwargs)
