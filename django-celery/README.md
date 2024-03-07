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

Visit [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/) for app development.


## Celery worker & Flower

Celery worker broker is using Redis.

Use Celery flower to monitor the worker, queue and job status.

Flower [`http://127.0.0.1:5000/`](http://127.0.0.1:5000/).


## Create superuser

Enter the `app` container,

```bash
$ docker-compose exec app bash
```

After entered into the container, then create a superuser for local development.

```bash
$ python manage.py createsuperuser
```

Then use the credentials to login to the admin page,

Admin [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)


## Celery results extension

Django celery results extension has been installed, and has db migration, you can check the tables on Admin panel.

* https://github.com/celery/django-celery-results
* https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html

Celery result: [127.0.0.1:8000/admin/django_celery_results/taskresult/](127.0.0.1:8000/admin/django_celery_results/taskresult/).
