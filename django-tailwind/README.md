# django-tailwind


A starter Django project with Tailwind CSS


## Setup Django Project

Create a Python virtual environment,

```bash
$ python3 -m venv .venv
```

Activate the virtual environment,

```bash
$ source .venv/bin/activate
```

Install Python packages,

```bash
$ pip install -r requirements.txt
```

## Setup Tailwind CSS

Make sure you have `node` and `npm` installed on your machine.

Enter
```bash
$ cd `django-tailwind`
```

Install `tailwindcss`

```bash
$ npm install tailwindcss
```

Init and configure Tailwind CSS,

```bash
$ npx tailwindcss init
```

This would create `tailwind.config.js`.


## Run Django Development Server

Run the following command to start the development server,

```bash
$ python manage.py runserver
```

Then visit [`http://127.0.0.1:8000`](http://127.0.0.1:8000)
