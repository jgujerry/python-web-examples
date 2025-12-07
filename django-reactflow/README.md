# Django Reactflow


## Setup development environment


Create a `.env` file in the root directory of this example with content below,

```text
DJANGO_SECRET_KEY='django-insecure--oe!c8quc8k@5vr+b=1cqwpzge*%gvr*r$uycx@7fx0xlc%g#8'
```

### Python Env

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



### Node Env

Create a node environment with `webpack`, which compiles React, React-dom and React flow into `bundle.js` and integrates into Django template.

Create node environment,

```bash
cd reactflow

npm install
```

Then start a new terminal session for watching and compiling,

```bash
npm run dev
```
