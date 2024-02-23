# flask-postgres

An example for project using flask and postgres stack.

Prerequisites:
* Docker
* Docker Compose


## Development Environment

Build images,
```bash
$ docker compose build
```

Run containers
```bash
$ docker compose up
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) for development.


## Attention Please

Here are some aspects that require attention, including potential tricks or pitfalls.

* Include `initdb.sql` to create the database.
* Set `PGUSER=postgres` to use user `postgres`, instead of `root`.
* Set `FLASK_APP` to let Flask-Migrate to find the app.
* Import models in `__init__.py` file so that Flask-Migrate could detect them.

Happy Coding!
