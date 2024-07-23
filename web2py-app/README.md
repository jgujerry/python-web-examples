# web2py-app


## Create a virtual environment

Run the following command to create a virtual environment

```bash
$ python3 -m venv .venv
```

then activate it,

```bash
$ source .venv/bin/activate
```

Clone Web2Py from its GitHub repo,

```bash
$ git clone https://github.com/web2py/web2py.git
```

Enter into the repository,

```bash
$ cd web2py
```

To ensure the submodules are inplace, then run

```bash
$ git submodule update --init --recursive
```

Then start Web2Py web portal,

```bash
$ python web2py.py
```

It'll require you to setup a password. After that, you can visit [http://127.0.0.1:8000](http://127.0.0.1:8000)


## Create a new project

Create a new project named `app` via the Web2Py UI, you can find it under `web2py/applications/app`.

Web2Py project has the following structure or layout,

```bash
app
├── ABOUT
├── controllers
├── cron
├── databases
├── errors
├── __init__.py
├── languages
├── LICENSE
├── models
├── modules
├── private
├── progress.log
├── routes.example.py
├── sessions
├── static
├── uploads
└── views

12 directories, 5 files
```

Then you can either develop the project using Web2Py web UI or maybe VSCode.

