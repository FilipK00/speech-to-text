# Use the official Python image as the base image
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Install system dependencies
RUN apt-get update && apt-get install -y \
    apt-utils \
    portaudio19-dev \
    python3-dev \
    gcc

# Install additional dependencies using conda
RUN apt-get install -y wget bzip2 \
    && wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh \
    && bash miniconda.sh -b -p /opt/conda \
    && rm miniconda.sh \
    && /opt/conda/bin/conda install -y -c conda-forge portaudio pyaudio \
    && apt-get clean -y && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*


# Install python3.X-pyaudio (adjust X to your Python version)
RUN apt-get install python3-pyaudio

# Install pyaudio for the Python environment
RUN pip install pyaudio

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run your application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--worker-tmp-dir", "/dev/shm", "speechai.wsgi:application"]
