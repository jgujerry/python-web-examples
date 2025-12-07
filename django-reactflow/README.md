# Django Reactflow


## Setup development environment

1. Python Env

Create a Python virtual environment by using `uv`,

```bash
uv venv .venv
```

Then install the required packages,

```bash
uv sync
```

Then start Django and visit [http://127.0.0.1:8000](http://127.0.0.1:8000)

```bash
python manage.py runserver
```



2. Node Env

Create a node environment with `webpack`, which compiles React, React-dom and React flow into `bundle.js` and integrates into Django template.

Create node environment,

```bash
cd reactflow

npm run dev
```
