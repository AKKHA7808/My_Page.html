#!/bin/bash

echo "🚀 Starting Vercel build process..."

# Set environment variables for build
export DJANGO_SETTINGS_MODULE=portfolio.settings.production
export DEBUG=False

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p /tmp

# Copy database to tmp (for Vercel)
echo "🗃️ Setting up database..."
if [ -f "db.sqlite3" ]; then
    cp db.sqlite3 /tmp/db.sqlite3
else
    # Create empty database if it doesn't exist
    python3 manage.py migrate --noinput
    cp db.sqlite3 /tmp/db.sqlite3
fi

# Collect static files
echo "🎨 Collecting static files..."
python3 manage.py collectstatic --noinput --clear

echo "✅ Build process completed successfully!"
