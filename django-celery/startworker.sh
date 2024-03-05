#!/usr/bin/env bash

celery --app config worker --hostname worker01 --loglevel info
