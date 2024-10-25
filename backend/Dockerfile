FROM python:slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project
COPY . .

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Specify the default command to run
ENTRYPOINT ["/app/entrypoint.sh"]
