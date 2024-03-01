#!/usr/bin/env bash

echo "Waiting for MongoDB..."

while ! nc -z $MONGO_HOST $MONGO_PORT; do
    sleep 0.5
done

echo "MongoDB started! Ready to recieve connections."

exec "$@"
