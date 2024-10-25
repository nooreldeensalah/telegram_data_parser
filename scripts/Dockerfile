# Use the official Python slim image from the Docker Hub
FROM python:slim

# Install required utilities including wget
RUN apt-get update && \
    apt-get install -y wget p7zip-full && \
    rm -rf /var/lib/apt/lists/*

# Manually download and install p7zip-rar
RUN wget http://ftp.debian.org/debian/pool/non-free/p/p7zip-rar/p7zip-rar_16.02-3_amd64.deb && \
    dpkg -i p7zip-rar_16.02-3_amd64.deb && \
    rm p7zip-rar_16.02-3_amd64.deb

# Set the working directory inside the container
WORKDIR /app

# Copy the Python scripts into the container
COPY . /app/

# Install any required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run the run_all.py script
CMD ["python", "run_all.py"]
