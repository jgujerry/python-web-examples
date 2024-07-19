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


## Create a Web2Py project


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
