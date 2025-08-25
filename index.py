import os
import sys

# Add project to Python path
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path)

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings.production')

# Django setup
import django
django.setup()

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application

# Create WSGI application
application = get_wsgi_application()

# Export for Vercel (this is what Vercel looks for)
app = application
