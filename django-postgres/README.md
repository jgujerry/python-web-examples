# django-postgres

This is a starter template for project using Django Postgres stack!

*Stack Information*

* *django 4.2.x*
* *postgresql latest*


The prerequisites of using this starter template are:

* [Docker](https://docs.docker.com/engine/install/)
* [Docker Compose](https://docs.docker.com/compose/install/)


## Dev Environment
Build docker images,

```bash
$ docker compose build
```

Up dev environment,
```bash
$ docker compose up
```

Visit [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/)


## More settings

Setup a virtual environment (e.g. `python -m venv .venv`), and activate it `source ./venv/bin/activate`.

```bash
$ pip install -r requirements-dev.txt
```

[`pre-commit`](https://pre-commit.com/) got installed,
 and will run git hook scripts for identifying code issues before git commit.

If you are using any IDE, then configure the IDE to use this virtual environment.
