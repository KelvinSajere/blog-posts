# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY src.python.task_manager.app/task_manager_pex_binary.pex /app.pex
ENTRYPOINT ["/app.pex"]
