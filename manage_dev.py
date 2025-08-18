#!/usr/bin/env python
"""
Development management utility for Django Portfolio project.
Extended version of manage.py with additional development features.
"""
import os
import sys
from pathlib import Path


def setup_development_environment():
    """Setup development environment settings."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
    os.environ.setdefault('DEBUG', 'True')
    

def run_development_server(port=8000):
    """Run Django development server with custom settings."""
    print(f"🚀 Starting Django Portfolio development server on port {port}...")
    print("📁 Project: Django Portfolio Website")
    print("🌐 Access at: http://127.0.0.1:{}/".format(port))
    print("💡 Press Ctrl+C to stop the server")
    print("-" * 50)
    
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage_dev.py', 'runserver', f'0.0.0.0:{port}'])


def run_migrations():
    """Run database migrations."""
    print("🔄 Running database migrations...")
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage_dev.py', 'migrate'])
    print("✅ Migrations completed!")


def collect_static():
    """Collect static files for deployment."""
    print("📦 Collecting static files...")
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage_dev.py', 'collectstatic', '--noinput'])
    print("✅ Static files collected!")


def create_superuser():
    """Create a superuser for admin access."""
    print("👤 Creating superuser...")
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage_dev.py', 'createsuperuser'])


def run_tests():
    """Run all tests."""
    print("🧪 Running tests...")
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage_dev.py', 'test'])


def show_urls():
    """Show all URL patterns."""
    print("🔗 Showing URL patterns...")
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage_dev.py', 'show_urls'])


def shell_plus():
    """Start Django shell with models pre-loaded."""
    print("🐍 Starting Django shell...")
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage_dev.py', 'shell'])


def dev_menu():
    """Show development menu."""
    print("\n" + "=" * 60)
    print("🎯 DJANGO PORTFOLIO - DEVELOPMENT MENU")
    print("=" * 60)
    print("1. Run Development Server (default port 8000)")
    print("2. Run Development Server (custom port)")
    print("3. Run Migrations")
    print("4. Collect Static Files")
    print("5. Create Superuser")
    print("6. Run Tests")
    print("7. Show URLs")
    print("8. Django Shell")
    print("9. Check System")
    print("0. Exit")
    print("-" * 60)
    
    choice = input("Select option (0-9): ").strip()
    
    if choice == '1':
        run_development_server()
    elif choice == '2':
        port = input("Enter port number (default 8000): ").strip() or "8000"
        run_development_server(int(port))
    elif choice == '3':
        run_migrations()
    elif choice == '4':
        collect_static()
    elif choice == '5':
        create_superuser()
    elif choice == '6':
        run_tests()
    elif choice == '7':
        show_urls()
    elif choice == '8':
        shell_plus()
    elif choice == '9':
        check_system()
    elif choice == '0':
        print("👋 Goodbye!")
        sys.exit(0)
    else:
        print("❌ Invalid option. Please try again.")
        dev_menu()


def check_system():
    """Run Django system check."""
    print("🔍 Running system check...")
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage_dev.py', 'check'])


def main():
    """Run administrative tasks with development enhancements."""
    setup_development_environment()
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # If no arguments provided, show development menu
    if len(sys.argv) == 1:
        dev_menu()
    else:
        # Handle specific commands
        if len(sys.argv) > 1:
            command = sys.argv[1].lower()
            
            if command == 'serve' or command == 'runserver':
                port = sys.argv[2] if len(sys.argv) > 2 else 8000
                run_development_server(int(port))
            elif command == 'migrate':
                run_migrations()
            elif command == 'static':
                collect_static()
            elif command == 'superuser':
                create_superuser()
            elif command == 'test':
                run_tests()
            elif command == 'urls':
                show_urls()
            elif command == 'shell':
                shell_plus()
            elif command == 'check':
                check_system()
            elif command == 'menu':
                dev_menu()
            else:
                # Run standard Django command
                execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
