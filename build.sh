#!/bin/bash

# Install dependencies
pip3 install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput

# Run migrations (if needed)
python3 manage.py migrate --noinput
