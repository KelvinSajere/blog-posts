# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY src.python.service_b.app/service_b_pex_binary.pex /
ENTRYPOINT ["/service_b_pex_binary.pex"]