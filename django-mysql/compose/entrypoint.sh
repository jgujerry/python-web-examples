#!/usr/bin/env bash

echo "Waiting for MySQL to start..."

while ! mysqladmin ping -h "db" --silent; do
    echo "Waiting for MySQL to be up..."
    sleep 1
done

echo "MySQL started!"

exec "$@"

echo "Starting the Django application..."
python manage.py collectstatic --noinput --clear

python manage.py migrate --noinput

python manage.py runserver 0.0.0.0:8000
