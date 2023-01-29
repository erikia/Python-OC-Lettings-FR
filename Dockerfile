FROM python:3.10-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install any necessary dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Start the server
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT

