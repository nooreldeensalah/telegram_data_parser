#!/bin/bash

# Run Django migrations
python manage.py migrate

# Create an initial user
python manage.py createinitialuser

# Start the Django server
python manage.py runserver 0.0.0.0:8000
