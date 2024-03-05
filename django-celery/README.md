# django-celery

This example shows how to create Django application with Celery.

The prerequisites of using the starter example are the following:

* [Docker](https://docs.docker.com/engine/install/)
* [Docker Compose](https://docs.docker.com/compose/install/)


## Development Environment

Enter the project directory, e.g.

```bash
$ cd django-celery
```

Create a Python virtual environment,
```bash
$ python -m venv .venv
```

Activate the virtual environment,
```bash
$ source .venv/bin/activate
```

For your IDE, point the Python interpreter to this `.venv`.


## Build and Run Containers
Build docker images,
```bash
$ docker compose build
```

Up dev environment,
```bash
$ docker compose up
```

Visit [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/)


