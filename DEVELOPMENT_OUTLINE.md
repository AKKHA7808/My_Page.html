# Django Portfolio Project - Development & Production Outline

## 📋 Table of Contents
1. [Development vs Production Settings](#development-vs-production-settings)
2. [Environment Configuration](#environment-configuration)
3. [Database Setup](#database-setup)
4. [Admin Configuration](#admin-configuration)
5. [Static Files Management](#static-files-management)
6. [Security Settings](#security-settings)
7. [Deployment Workflow](#deployment-workflow)
8. [Monitoring & Logging](#monitoring--logging)

---

## 🔧 Development vs Production Settings

### Development Environment
```python
# settings/development.py
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

# Database - SQLite for development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Email - Console backend for testing
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Security - Relaxed for development
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
```

### Production Environment
```python
# settings/production.py
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com']

# Database - PostgreSQL for production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# Email - Real SMTP for production
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Security - Strict for production
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
```

---

## 🌍 Environment Configuration

### .env Files Structure
```
# .env.development
DEBUG=True
SECRET_KEY=your-dev-secret-key
DATABASE_URL=sqlite:///db.sqlite3

# .env.production
DEBUG=False
SECRET_KEY=your-production-secret-key
DATABASE_URL=postgresql://user:pass@host:port/dbname
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### Settings Organization
```
portfolio/
├── settings/
│   ├── __init__.py
│   ├── base.py          # Common settings
│   ├── development.py   # Development specific
│   ├── production.py    # Production specific
│   └── testing.py       # Testing specific
└── manage.py
```

---

## 🗃️ Database Setup

### SQLite (Development)
```python
# Good for development, single file database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### PostgreSQL (Production)
```python
# Robust for production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfolio_db',
        'USER': 'portfolio_user',
        'PASSWORD': 'secure_password',
        'HOST': 'localhost',
        'PORT': '5432',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}
```

### Database Commands
```bash
# Development
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata fixtures/initial_data.json

# Production
python manage.py migrate --settings=portfolio.settings.production
python manage.py collectstatic --noinput
```

---

## 👤 Admin Configuration

### Admin User Setup
```python
# Create superuser
python manage.py createsuperuser
# Username: admin
# Email: admin@portfolio.com
# Password: secure_admin_password
```

### Admin Customization
```python
# main/admin.py
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class PortfolioAdminSite(admin.AdminSite):
    site_header = 'Portfolio Administration'
    site_title = 'Portfolio Admin'
    index_title = 'Welcome to Portfolio Admin'

admin_site = PortfolioAdminSite(name='portfolio_admin')

# Custom User Admin
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_joined')
    search_fields = ('username', 'first_name', 'last_name', 'email')

admin_site.register(User, UserAdmin)
```

### Admin Security
```python
# settings/base.py
ADMIN_URL = os.environ.get('ADMIN_URL', 'admin/')

# urls.py
urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
]
```

---

## 📁 Static Files Management

### Development
```python
# Static files served by Django
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### Production
```python
# Static files served by CDN/WhiteNoise
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# WhiteNoise configuration
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files (use cloud storage)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
```

---

## 🔒 Security Settings

### Development Security
```python
# Relaxed for development
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

# Debug toolbar
if DEBUG:
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
```

### Production Security
```python
# Strict security headers
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "https://your-domain.com",
    "https://www.your-domain.com",
]
```

---

## 🚀 Deployment Workflow

### Local Development
```bash
# 1. Setup virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# 2. Install dependencies
pip install -r requirements/development.txt

# 3. Setup database
python manage.py migrate

# 4. Create superuser
python manage.py createsuperuser

# 5. Run development server
python manage_dev.py serve
```

### Production Deployment
```bash
# 1. Prepare production environment
export DJANGO_SETTINGS_MODULE=portfolio.settings.production

# 2. Install production dependencies
pip install -r requirements/production.txt

# 3. Collect static files
python manage.py collectstatic --noinput

# 4. Run migrations
python manage.py migrate

# 5. Start production server
gunicorn portfolio.wsgi:application
```

---

## 📊 Monitoring & Logging

### Development Logging
```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}
```

### Production Logging
```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/error.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
```

---

## 📚 Additional Resources

### Required Packages
```txt
# requirements/base.txt
Django==5.1.4
python-decouple==3.8
whitenoise==6.8.2

# requirements/development.txt
-r base.txt
django-debug-toolbar==4.4.6
django-extensions==3.2.3

# requirements/production.txt
-r base.txt
gunicorn==23.0.0
psycopg2-binary==2.9.9
sentry-sdk==1.45.0
```

### Environment Variables
```bash
# Essential environment variables
SECRET_KEY=your-secret-key
DEBUG=True/False
DATABASE_URL=database-connection-string
ALLOWED_HOSTS=comma,separated,hosts
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=your-email
EMAIL_HOST_PASSWORD=your-password
ADMIN_URL=custom-admin-path/
```

---

## 🎯 Quick Commands Reference

```bash
# Development
python manage_dev.py                    # Show development menu
python manage_dev.py serve              # Run development server
python manage_dev.py migrate            # Run migrations
python manage_dev.py shell              # Django shell

# Production
python manage.py migrate --settings=portfolio.settings.production
python manage.py collectstatic --noinput --settings=portfolio.settings.production
python manage.py createsuperuser --settings=portfolio.settings.production

# Database
python manage.py makemigrations         # Create new migrations
python manage.py showmigrations         # Show migration status
python manage.py sqlmigrate app_name 0001  # Show SQL for migration

# Admin
python manage.py changepassword username  # Change user password
python manage.py loaddata fixture.json    # Load data from fixture
python manage.py dumpdata app.model       # Export data to fixture
```

---

**📝 Note**: This outline provides a comprehensive structure for managing Django Portfolio project across different environments with proper security, database management, and admin configuration.
