from jinja2 import Environment, FileSystemLoader


def render(template_name, **kwargs):
    env = Environment(loader=FileSystemLoader("./templates"))
    template = env.get_template(template_name)
    return template.render(**kwargs)
