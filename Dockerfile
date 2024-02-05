# Use the official Python image as the base image
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install system dependencies
RUN apt-get update && apt-get install -y \
    portaudio19-dev \
    python3-dev

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run your application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "speechai.wsgi:application"]