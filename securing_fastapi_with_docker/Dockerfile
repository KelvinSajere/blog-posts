# Step 1: Use an official Python slim runtime based on Debain
FROM python@sha256:590aa200bf472f2b15eb5b72bbe20410ddeee30c79c2c306c1c83ee315cd1efb

# Step 2: Create a non-root user with specified UID and GID
RUN groupadd -r mygroup && useradd -r -g mygroup myuser

#Step 3: Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Step 4: Set the working directory to /app
WORKDIR /app

#Step 5: Copy only the requirements file to leverage Docker cache
COPY requirements.txt /app/

#Step 6: Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

#Step 7: Copy the rest of the application code
COPY . /app/

#Step 8: Change ownership of the /app directory to the non-root user
RUN chown -R myuser:mygroup /app

#Step 9:  Switch to the non-root user
USER myuser

#Step 10:  Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]