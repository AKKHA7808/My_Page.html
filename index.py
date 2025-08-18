import os
import sys

# Add project to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings.production')
os.environ.setdefault('DEBUG', 'False')

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application

# Create application
application = get_wsgi_application()

# Export for Vercel
app = application
