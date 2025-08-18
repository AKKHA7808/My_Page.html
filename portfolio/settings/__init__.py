"""
Settings package initialization.
Automatically loads appropriate settings based on environment.
"""

import os

# Determine which settings to use
env = os.environ.get('DJANGO_ENV', 'development')

if env == 'production':
    from .production import *
elif env == 'testing':
    from .testing import *
else:
    from .development import *

print(f"⚙️  Loaded settings: {env}")
