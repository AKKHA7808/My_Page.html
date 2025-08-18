"""
Alternative entry point for Vercel deployment.
This provides multiple ways for Vercel to find the application.
"""

from index import app, application, handler

# Multiple export names for compatibility
main = app
default = app
vercel_app = app

# Function-based exports
def main_handler(event, context):
    """Main handler function."""
    return handler(event, context)

def app_handler(event, context):
    """App handler function."""
    return application(event, context)
