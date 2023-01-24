FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED=1

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install any necessary dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# # Expose port 8000 for the web server to listen on
# EXPOSE 8000

# Start the server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["gunicorn", "--bind", , ":8000", "--workers", "3", "core.wsgi:application"]
# CMD gunicorn core.wsgi:application --bind 0.0.0.0:$PORT
