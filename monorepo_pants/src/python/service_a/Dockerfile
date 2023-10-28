# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY src.python.service_a.app/service_a_pex_binary.pex /app.pex
ENTRYPOINT ["/app.pex"]
