"""
Development settings for Django Portfolio project.
Settings for local development environment.
"""

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0', '*']

# Database - SQLite for development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Email settings for development - Console backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Security settings for development (relaxed)
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# Development-specific apps
INSTALLED_APPS += [
    # Add development tools here
    # 'debug_toolbar',  # Uncomment if installed
    # 'django_extensions',  # Uncomment if installed
]

# Development middleware
# if 'debug_toolbar' in INSTALLED_APPS:
#     MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
#     INTERNAL_IPS = ['127.0.0.1']

# Cache settings for development
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Static files - Django serves them in development
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Development logging - more verbose
LOGGING['handlers']['console']['level'] = 'DEBUG'
LOGGING['loggers']['django']['level'] = 'DEBUG'

# Add custom logging for development
LOGGING['loggers'].update({
    'main': {
        'handlers': ['console'],
        'level': 'DEBUG',
        'propagate': True,
    },
    'portfolio': {
        'handlers': ['console'],
        'level': 'DEBUG',
        'propagate': True,
    }
})

print("🔧 Running in DEVELOPMENT mode")
print(f"📁 BASE_DIR: {BASE_DIR}")
print(f"🗃️  Database: SQLite at {DATABASES['default']['NAME']}")
print(f"🎯 Debug: {DEBUG}")
