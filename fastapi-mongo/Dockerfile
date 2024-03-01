FROM python:3.12-slim-bookworm

# Set environment variables
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PYTHONNUNBUFFERED=TRUE

# Install system dependencies
RUN apt-get update -y --fix-missing \
    && apt-get install -y --no-install-recommends \
    build-essential \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get autoclean

# Install python packages
WORKDIR /src
COPY ./requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# File operations
COPY ./wait-for-mongo.sh /wait-for-mongo.sh
RUN chmod +x /wait-for-mongo.sh
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Copy All code
COPY . .
