"""
WSGI config for portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set Django settings for production on Vercel
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings.production')
os.environ.setdefault('DJANGO_ENV', 'production')
os.environ.setdefault('DEBUG', 'False')

# Initialize Django
application = get_wsgi_application()

# Vercel compatibility
app = application

# For Vercel deployment
def handler(request, context):
    """Vercel serverless function handler."""
    return application(request, context)
