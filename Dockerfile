# Pull base image
FROM python:3

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y && apt-get autoremove \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
RUN mkdir -p /diploma
WORKDIR /diploma

# Install dependencies
RUN pip install --upgrade pip
COPY diploma/requirements/base.txt .
RUN pip install -r base.txt

# Copy project
COPY . /diploma/

# Server
#EXPOSE 8000
STOPSIGNAL SIGINT