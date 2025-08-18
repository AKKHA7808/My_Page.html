"""
Production settings for Django Portfolio project.
Settings for production environment (Vercel, Heroku, etc.).
"""

from .base import *
# Remove dj_database_url import since it's not installed yet
# import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Allowed hosts for production
ALLOWED_HOSTS = [
    'your-domain.com',
    'www.your-domain.com',
    '.vercel.app',  # For Vercel deployment
    '.herokuapp.com',  # For Heroku deployment
]

# Database - PostgreSQL for production (fallback to SQLite)
if 'DATABASE_URL' in os.environ:
    # For when dj-database-url is installed
    # DATABASES = {
    #     'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    # }
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    # Fallback to SQLite for Vercel
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Email settings for production
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', '587'))
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', EMAIL_HOST_USER)

# Security settings for production
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Additional security headers
SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'
SECURE_CROSS_ORIGIN_OPENER_POLICY = 'same-origin'

# Cache settings for production
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': os.environ.get('REDIS_URL', 'redis://127.0.0.1:6379/1'),
    }
} if os.environ.get('REDIS_URL') else {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# Session configuration
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

# Production logging - file-based
LOGGING['handlers'].update({
    'file': {
        'level': 'ERROR',
        'class': 'logging.FileHandler',
        'filename': os.path.join(BASE_DIR, 'logs', 'django.log'),
        'formatter': 'verbose',
    },
})

LOGGING['loggers'].update({
    'django': {
        'handlers': ['console', 'file'],
        'level': 'WARNING',
        'propagate': False,
    },
    'main': {
        'handlers': ['file'],
        'level': 'ERROR',
        'propagate': True,
    },
})

# Static files for production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files - use cloud storage in production
if os.environ.get('AWS_STORAGE_BUCKET_NAME'):
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME', 'us-east-1')

print("🚀 Running in PRODUCTION mode")
print(f"🌐 Allowed hosts: {ALLOWED_HOSTS}")
print(f"🗃️  Database: {'PostgreSQL' if 'DATABASE_URL' in os.environ else 'SQLite'}")
print(f"🔒 SSL Redirect: {SECURE_SSL_REDIRECT}")
