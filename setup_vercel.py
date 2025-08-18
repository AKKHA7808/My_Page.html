#!/usr/bin/env python3
"""
Setup script for Vercel auto deployment.
This script helps configure Vercel for automatic deployment.
"""

import subprocess
import sys
import os

def run_command(command, description="Running command"):
    """Run a shell command and handle errors."""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error in {description}:")
        print(e.stderr)
        return False

def check_vercel_cli():
    """Check if Vercel CLI is installed."""
    try:
        result = subprocess.run("vercel --version", shell=True, check=True, capture_output=True, text=True)
        print(f"✅ Vercel CLI found: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError:
        print("❌ Vercel CLI not found")
        return False

def install_vercel_cli():
    """Install Vercel CLI."""
    print("📦 Installing Vercel CLI...")
    if run_command("npm install -g vercel", "Installing Vercel CLI"):
        return True
    else:
        print("💡 Please install Vercel CLI manually:")
        print("   npm install -g vercel")
        return False

def setup_vercel_project():
    """Setup Vercel project."""
    print("🔧 Setting up Vercel project...")
    
    # Login to Vercel
    if not run_command("vercel login", "Logging into Vercel"):
        print("❌ Failed to login to Vercel")
        return False
    
    # Link project
    if not run_command("vercel link", "Linking project to Vercel"):
        print("❌ Failed to link project")
        return False
    
    # Set environment variables
    print("⚙️ Setting environment variables...")
    env_vars = [
        "DEBUG=False",
        "DJANGO_ENV=production",
        "DJANGO_SETTINGS_MODULE=portfolio.settings.production"
    ]
    
    for env_var in env_vars:
        key, value = env_var.split("=", 1)
        run_command(f'vercel env add {key} production', f"Setting {key}")
    
    return True

def main():
    """Main setup function."""
    print("🚀 Vercel Auto Deployment Setup")
    print("=" * 50)
    
    # Check Node.js
    if not run_command("node --version", "Checking Node.js"):
        print("❌ Node.js not found. Please install Node.js first.")
        return
    
    # Check or install Vercel CLI
    if not check_vercel_cli():
        if not install_vercel_cli():
            return
    
    # Setup project
    if setup_vercel_project():
        print("\n🎉 Vercel auto deployment setup completed!")
        print("💡 Next steps:")
        print("   1. Push your code to GitHub")
        print("   2. Vercel will automatically deploy")
        print("   3. Check your Vercel dashboard for deployment status")
        print("\n🔗 Useful commands:")
        print("   vercel --prod     # Manual production deployment")
        print("   vercel logs       # View deployment logs")
        print("   vercel domains    # Manage custom domains")
    else:
        print("❌ Setup failed. Please check the errors above.")

if __name__ == '__main__':
    main()
