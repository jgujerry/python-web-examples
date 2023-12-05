#!/usr/bin/env bash

echo "Waiting for PostgreSQL to start..."

while ! pg_isready -h $POSTGRES_HOST -p $POSTGRES_PORT; do
  sleep 1
done

echo "PostgreSQL started!"

exec "$@"


echo "Starting the Bottle application..."
python app/main.py
