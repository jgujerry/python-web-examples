#!/usr/bin/env bash

echo "Waiting for MySQL to start..."

while ! mysqladmin ping -h "db" --silent; do
    echo "Waiting for MySQL to be up..."
    sleep 1
done

echo "MySQL started!"

exec "$@"


echo "Starting the Bottle application..."
python app/main.py
