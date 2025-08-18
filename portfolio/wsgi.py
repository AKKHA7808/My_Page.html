"""
WSGI config for portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path

# Add the project directory to Python path
PROJECT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_DIR))

# Set Django settings for production on Vercel
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings.production')
os.environ.setdefault('DJANGO_ENV', 'production')
os.environ.setdefault('DEBUG', 'False')

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application

# Initialize Django
try:
    application = get_wsgi_application()
except Exception as e:
    print(f"Error initializing Django application: {e}")
    # Fallback for debugging
    import traceback
    traceback.print_exc()
    raise

# Vercel compatibility
app = application

# Handler for Vercel serverless functions
def handler(event, context):
    """Serverless function handler for Vercel."""
    return application(event, context)
