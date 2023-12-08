#!/usr/bin/env bash

echo "Waiting for PostgreSQL to start..."

while ! pg_isready -h $POSTGRES_HOST -p $POSTGRES_PORT; do
  sleep 1
done

echo "PostgreSQL started!"

exec "$@"

echo "Starting the Django application..."
python manage.py collectstatic --noinput --clear

python manage.py migrate --noinput

python manage.py runserver 0.0.0.0:8000
