import os
import sys
import django
from django.core.wsgi import get_wsgi_application

# Add project to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings.production')
os.environ.setdefault('DEBUG', 'False')

# Setup Django
django.setup()

# Create WSGI application
application = get_wsgi_application()

# Export for Vercel
app = application

def handler(request):
    """Handler function for Vercel"""
    return app(request.environ, request.start_response)
