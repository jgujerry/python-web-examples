import pathlib


APP_DIR = pathlib.Path(__file__).parents[1].absolute()

TEMPLATE_DIR = APP_DIR.joinpath('templates')

STATIC_ROOTDIR = APP_DIR.joinpath('static')
