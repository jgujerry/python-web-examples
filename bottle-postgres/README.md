# bottle-postgres
A starter template for project using Bottle/Postgres

*Stack Information*

* *Bottle 0.12*
* *Postgres latest*


## Prerequisites

* [Docker](https://docs.docker.com/engine/install/)
* [Docker Compose](https://docs.docker.com/compose/install/)


## Local Environment Setup

Get this starter template,
```bash
$ cd bottle-postgres
```

Build docker image,
```bash
$ docker compose build
```

Run docker compose services,
```bash
$ docker compose up
```

Then visit `127.0.0.1:8080`

## Postgres Container

After docker compose is up, then you can enter the Postgres container. Open another terminal session and run

```bash
$ docker compose exec db bash
```

which would let you enter the bash shell of Postgres container. Then run `psql` command to connect the database.

```bash
$ psql --host localhost --port 5432 --user postgres
```

Afte enter the Postgres container, then you can run postgresql queries, e.g.

```bash
postgres=# \l
                                                List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    | ICU Locale | Locale Provider |   Access privileges   
-----------+----------+----------+------------+------------+------------+-----------------+-----------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgres          +
           |          |          |            |            |            |                 | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgres          +
           |          |          |            |            |            |                 | postgres=CTc/postgres
(3 rows)
```

To exit psql command line, type `\q` command.


## Code Quality Control

`pre-commit` is introduced into this project for code quality control.

Create your local virtual environment, then please run 
```bash
pip install -r requirements-dev.txt
``` 
to install packages for dev, including `pre-commit`.

To customize pre-commit config, please update the `.pre-commit.config.yaml` file.

## Note

At the time of writing, `sqlalchemy` does not support `psycopg3` yet, so to use `psycopg2` here.

If you are using any IDE, then configure the IDE to use this virtual environment.
