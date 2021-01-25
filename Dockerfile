#Docker file

# Languaje used
FROM python:3.8

# set environment variables
ENV PYTHONUNBUFFERED=1

# set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy project container
COPY . /code/