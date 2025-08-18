"""
Vercel entry point for Django application.
This file serves as the main entry point for Vercel deployment.
"""

import os
import sys
from pathlib import Path

# Add project to Python path
PROJECT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_DIR))

# Set environment variables
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings.production')
os.environ.setdefault('DJANGO_ENV', 'production')
os.environ.setdefault('DEBUG', 'False')

# Import and setup Django
try:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
except Exception as e:
    print(f"Error initializing Django: {e}")
    import traceback
    traceback.print_exc()
    raise

# Export for Vercel
app = application

# Alternative handler names for Vercel
handler = application
index = application
