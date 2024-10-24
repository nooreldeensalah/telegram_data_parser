# Use the official Python image from the Docker Hub
FROM python:slim

# Install `7z`
RUN apt-get update && apt-get install -y p7zip-full && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the Python scripts into the container
COPY . /app/

# Install any required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run the run_all.py script
CMD ["python", "run_all.py"]
