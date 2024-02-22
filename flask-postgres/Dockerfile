# Use an official Python runtime based on Debian 11 "bullseye" as a parent image.
FROM python:3.12-slim-bookworm

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV DEBIAN_FRONTED=noniteractive
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PYTHONUNBUFFERED=TRUE


# Port used by this container to serve HTTP.
EXPOSE 5000

# Install system packages
RUN apt-get update --yes --quiet && \
    apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    postgresql-client && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get autoclean

# Use /web folder as a directory where the source code is stored.
WORKDIR /web

# Install the application server.
RUN pip install --upgrade pip

# Install the project requirements.
COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

# Copy the source code of the project into the container.
COPY . .
RUN chmod +x ./entrypoint.sh
