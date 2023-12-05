# Use an official Python runtime based on Debian 11 "bullseye" as a parent image.
FROM python:3.10-slim-bullseye

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV DEBIAN_FRONTED=noniteractive
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PYTHONUNBUFFERED=TRUE

# Add user that will be used in the container.
RUN useradd appuser

# Port used by this container to serve HTTP.
EXPOSE 8080

# Install system packages
RUN apt-get update --yes --quiet && \
    apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    postgresql-client && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get autoclean


# Use /src folder as a directory where the source code is stored.
# Set this directory to be owned by the "appuser" user.
WORKDIR /src
RUN chown appuser:appuser /src

# Install the application server.
RUN pip install --upgrade pip

# Install the project requirements.
COPY ./requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt

# Copy the source code of the project into the container.
COPY --chown=appuser:appuser . .

# Use user "appuser" to run the build commands below and the server itself.
USER appuser
