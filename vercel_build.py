#!/usr/bin/env python3
"""
Build script for Vercel deployment.
This script handles the build process for Django on Vercel.
"""

import os
import sys
import subprocess

def run_command(command, description="Running command"):
    """Run a shell command and handle errors."""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error in {description}:")
        print(e.stderr)
        return False

def main():
    """Main build function for Vercel."""
    print("🚀 Starting Vercel build process...")
    
    # Set environment variables for production
    os.environ['DJANGO_ENV'] = 'production'
    os.environ['DEBUG'] = 'False'
    
    # Install requirements
    print("📦 Installing dependencies...")
    if not run_command("pip install -r requirements.txt", "Installing Python packages"):
        sys.exit(1)
    
    # Set Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings.production')
    
    # Import Django and setup
    try:
        import django
        django.setup()
    except ImportError:
        print("❌ Django not installed properly")
        sys.exit(1)
    
    # Run migrations
    print("🗃️ Running database migrations...")
    if not run_command("python manage.py migrate --noinput", "Database migrations"):
        print("⚠️ Migration failed, continuing...")
    
    # Collect static files
    print("📁 Collecting static files...")
    if not run_command("python manage.py collectstatic --noinput", "Static files collection"):
        print("⚠️ Static files collection failed, continuing...")
    
    print("✅ Vercel build completed successfully!")

if __name__ == '__main__':
    main()
