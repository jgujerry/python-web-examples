# django-mysql

A starter example for project using Django/MySQL


*Stack Information*

* *django 4.2.x*
* *mysql latest*


The rrerequisites of using this starter example:

* [Docker](https://docs.docker.com/engine/install/)
* [Docker Compose](https://docs.docker.com/compose/install/)


## Dev Environment

Clone this repository, and get into the `django-mysql` directory,

```bash
cd django-mysql
```

Build docker images,

```bash
$ docker compose build
```

Up dev environment,
```bash
$ docker compose up
```

Visit [`http://127.0.0.1:8000/`](`http://127.0.0.1:8000/`)


## More settings

Setup a virtual environment (e.g. `python -m venv .venv`), and activate it `source ./venv/bin/activate`.

```bash
$ pip install -r requirements-dev.txt
```

[`pre-commit`](https://pre-commit.com/) got installed,
 and will run git hook scripts for identifying code issues before git commit.

If you are using any IDE, then configure the IDE to use this virtual environment.
