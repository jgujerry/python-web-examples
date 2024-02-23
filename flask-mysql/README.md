# flask-mysql

An example for project using flask and mysql stack.

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
* Set `FLASK_APP` to let Flask-Migrate to find the app.
* Import models in `__init__.py` file so that Flask-Migrate could detect them.
* You need to specify one of the following as an environment variable:
  - MYSQL_ROOT_PASSWORD [Used here]
  - MYSQL_ALLOW_EMPTY_PASSWORD
  - MYSQL_RANDOM_ROOT_PASSWORD
* VARCHAR requires a length on dialect mysql

## Database Migration

Get into the container
```bash
$ docker compose exec web bash
```

Use the following commands to migrate your database

Init database (Already inited, you could skip this step)
```bash
$ flask db init
```

Migrate to create versions,
```bash
$ flask db migrate
```

Then upgrade new versions,
```bash
$ flask db upgrade
```

Happy Coding!
