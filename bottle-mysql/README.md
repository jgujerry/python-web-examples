# bottle-mysql
A starter example for project using Bottle/MySQL database.

*Stack Information*

* *bottle 0.12*
* *MySQL latest*


The prerequisites of this starter example,

* [Docker](https://docs.docker.com/engine/install/)
* [Docker Compose](https://docs.docker.com/compose/install/)


## Dev environment

Clone this repository,

```bash
$ cd bottle-mysql
```

Build docker image,
```bash
$ docker compose build
```

Run docker compose services,
```bash
$ docker compose up
```

Then visit [`http://127.0.0.1:8080`](http://127.0.0.1:8080)

## MySQL container

After docker compose is up, then you can enter the MySQL container. Open another terminal session and run

```bash
$ docker compose exec db bash
```

which would let you enter the bash shell of MySQL container. Then run `mysql` command to connect the database.

```bash
$ mysql --host localhost --port 3306 --user root --password
```

The password is `123456` here. Afte enter the MySQL container, then you can run mysql queries, e.g.

```bash
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| devdb              |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)
```

To exit the mysql command line, type `exit`.


## More settings

`pre-commit` is introduced into this project for code quality control.

Create your local virtual environment, then please run 
```bash
pip install -r requirements-dev.txt
``` 
to install packages for dev, including `pre-commit`.

To customize pre-commit config, please update the `.pre-commit.config.yaml` file.

If you are using any IDE, then configure the IDE to use this virtual environment.
