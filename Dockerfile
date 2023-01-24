FROM python:3.10-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install any necessary dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Start the server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

