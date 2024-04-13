# pyramid-app


## Introduction

This project got initialized by using `cookiecutter`.

```bash
$ cookiecutter gh:Pylons/pyramid-cookiecutter-starter 

  [1/4] project_name (Pyramid Scaffold): pyramid-app
  [2/4] repo_name (pyramid_app): 
  [3/4] Select template_language
    1 - jinja2
    2 - chameleon
    3 - mako
    Choose from [1/2/3] (1): 
  [4/4] Select backend
    1 - none
    2 - sqlalchemy
    3 - zodb
    Choose from [1/2/3] (1): 

===============================================================================
Documentation: https://docs.pylonsproject.org/projects/pyramid/en/latest/
Tutorials:     https://docs.pylonsproject.org/projects/pyramid_tutorials/en/latest/
Twitter:       https://twitter.com/PylonsProject
Mailing List:  https://groups.google.com/forum/#!forum/pylons-discuss
Welcome to Pyramid.  Sorry for the convenience.
===============================================================================

Change directory into your newly created project.
    cd pyramid-app

Create a Python virtual environment.
    python3 -m venv .venv

Upgrade packaging tools.
    env/bin/pip install --upgrade pip setuptools

Install the project in editable mode with its testing requirements.
    env/bin/pip install -e ".[testing]"

Run your project's tests.
    env/bin/pytest

Run your project.
    env/bin/pserve development.ini
```

## Setup Development Environment

Create a virtual environment,

```bash
$ python3 -m venv .venv
```

Then upgrade the `pip` and `setuptools` if need,

```bash
$ pip install -U pip setuptools
```

Install required packages into the virtual environment,

```bash
$ python setup.py develop
```

Then visit the site [`http://127.0.0.1:6543/`](http://127.0.0.1:6543/)
