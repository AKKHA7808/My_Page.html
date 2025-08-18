"""
Debug script to test Django setup on Vercel.
This will help identify issues with the deployment.
"""

import os
import sys
import traceback
from pathlib import Path

def debug_django():
    """Debug Django setup."""
    print("🔍 Django Debug Information")
    print("=" * 50)
    
    # Environment info
    print(f"Python version: {sys.version}")
    print(f"Python path: {sys.path}")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Project directory: {Path(__file__).resolve().parent}")
    
    # Environment variables
    print("\n📋 Environment Variables:")
    for key in ['DJANGO_SETTINGS_MODULE', 'DJANGO_ENV', 'DEBUG', 'PYTHONPATH']:
        print(f"{key}: {os.environ.get(key, 'Not set')}")
    
    # Try to import Django
    print("\n🐍 Django Import Test:")
    try:
        import django
        print(f"✅ Django version: {django.get_version()}")
        
        # Set settings module
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings.production')
        
        # Setup Django
        django.setup()
        print("✅ Django setup completed")
        
        # Test settings
        from django.conf import settings
        print(f"✅ Settings loaded: {settings.SETTINGS_MODULE}")
        print(f"✅ Debug mode: {settings.DEBUG}")
        print(f"✅ Allowed hosts: {settings.ALLOWED_HOSTS}")
        
        # Test WSGI
        from django.core.wsgi import get_wsgi_application
        application = get_wsgi_application()
        print("✅ WSGI application created")
        
        return application
        
    except Exception as e:
        print(f"❌ Error: {e}")
        traceback.print_exc()
        return None

if __name__ == "__main__":
    debug_django()
