# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Install system dependencies required for opencv-python, face-recognition, mysqlclient, and psycopg2
RUN apt-get update && apt-get install -y \
    cmake \
    libboost-all-dev \
    libgtk2.0-dev \
    libgl1-mesa-glx \
    libglib2.0-0 \
    default-libmysqlclient-dev \
    gcc \
    pkg-config \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and setuptools
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

# Copy the requirements.txt and install Python dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . /code/
