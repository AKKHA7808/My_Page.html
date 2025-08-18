#!/usr/bin/env python
"""
Quick setup script for Django Portfolio project.
This script will help you set up the project quickly.
"""
import os
import sys
import subprocess

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"📋 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during {description}:")
        print(e.stderr)
        return False

def main():
    """Main setup function."""
    print("🎯 Django Portfolio - Quick Setup")
    print("=" * 50)
    
    # Check if virtual environment is activated
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("⚠️  Virtual environment not detected!")
        print("💡 Consider activating your virtual environment first.")
    
    # Install requirements
    if not run_command("pip install -r requirements.txt", "Installing requirements"):
        print("❌ Failed to install requirements. Please check your environment.")
        return
    
    # Make migrations
    if not run_command("python manage.py makemigrations", "Creating migrations"):
        print("❌ Failed to create migrations.")
        return
    
    # Run migrations
    if not run_command("python manage.py migrate", "Running migrations"):
        print("❌ Failed to run migrations.")
        return
    
    # Collect static files
    if not run_command("python manage.py collectstatic --noinput", "Collecting static files"):
        print("⚠️  Failed to collect static files (this is optional for development).")
    
    # Check if superuser exists
    print("\n👤 Setting up admin user...")
    create_superuser = input("Do you want to create a superuser? (y/n): ").lower().strip()
    
    if create_superuser in ['y', 'yes']:
        if not run_command("python manage.py createsuperuser", "Creating superuser"):
            print("⚠️  Failed to create superuser. You can create one later with 'python manage.py createsuperuser'")
    
    # Final message
    print("\n" + "=" * 50)
    print("🎉 Setup completed successfully!")
    print("💡 Next steps:")
    print("   1. Copy .env.example to .env and update your settings")
    print("   2. Run 'python manage_dev.py' to start development server")
    print("   3. Visit http://127.0.0.1:8000/ to see your portfolio")
    print("   4. Visit http://127.0.0.1:8000/admin/ to access admin panel")
    print("=" * 50)

if __name__ == '__main__':
    main()
