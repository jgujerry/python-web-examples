# bottle-postgres
A starter template for project using Bottle/Postgres

*Stack Information*

* *bottle 0.12*
* *postgres latest*


The prerequisites of using the starter template are the following:

* [Docker](https://docs.docker.com/engine/install/)
* [Docker Compose](https://docs.docker.com/compose/install/)


## Local dev environment

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

## Check Postgres container

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

## More dev settings

`pre-commit` is introduced into this project for code quality control.

Create your local virtual environment, then please run 
```bash
pip install -r requirements-dev.txt
``` 
to install packages for dev, including `pre-commit`.

To customize pre-commit config, please update the `.pre-commit.config.yaml` file.


Happy coding!
