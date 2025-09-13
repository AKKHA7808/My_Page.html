#!/bin/bash

# Script to push the Django Portfolio to Otop-Thailand repository
# This script helps commit and push the current Django portfolio website 
# to the Otop-Thailand GitHub repository

echo "🚀 Django Portfolio to Otop-Thailand Push Script"
echo "================================================"

# Check if we're in the right directory
if [ ! -f "manage.py" ]; then
    echo "❌ Error: This script must be run from the Django project root directory"
    exit 1
fi

# Check if otop-thailand remote exists
if ! git remote | grep -q "otop-thailand"; then
    echo "❌ Error: otop-thailand remote not found"
    echo "Run: git remote add otop-thailand https://github.com/AKKHA7808/Otop-Thailand.git"
    exit 1
fi

echo "📂 Current repository: $(git remote get-url origin)"
echo "📂 Target repository: $(git remote get-url otop-thailand)"
echo ""

# Get current branch
CURRENT_BRANCH=$(git branch --show-current)
echo "📍 Current branch: $CURRENT_BRANCH"

# Check for uncommitted changes
if ! git diff-index --quiet HEAD --; then
    echo "⚠️  Warning: You have uncommitted changes"
    echo "Would you like to commit them first? (y/n)"
    read -r response
    if [[ "$response" =~ ^[Yy]$ ]]; then
        echo "💬 Enter commit message:"
        read -r commit_message
        git add .
        git commit -m "$commit_message"
        echo "✅ Changes committed"
    else
        echo "❌ Please commit your changes before pushing to otop-thailand"
        exit 1
    fi
fi

echo ""
echo "🔄 Preparing to push to otop-thailand repository..."
echo "This will push the current branch '$CURRENT_BRANCH' to the otop-thailand remote"
echo ""
echo "⚠️  WARNING: This will create or update the branch in the Otop-Thailand repository"
echo "Continue? (y/n)"
read -r confirm

if [[ "$confirm" =~ ^[Yy]$ ]]; then
    echo "🚀 Pushing to otop-thailand remote..."
    
    # Push to otop-thailand remote
    if git push otop-thailand "$CURRENT_BRANCH"; then
        echo ""
        echo "✅ Successfully pushed to Otop-Thailand repository!"
        echo "🌐 View at: https://github.com/AKKHA7808/Otop-Thailand"
        echo ""
        echo "📁 Repository now contains Django Portfolio Website with:"
        echo "   - Django 5.1.4 application"
        echo "   - Glass morphism design"
        echo "   - Thai language content"
        echo "   - Bootstrap 5 responsive layout"
        echo "   - Portfolio sections: Home, About, Contact"
    else
        echo "❌ Failed to push to otop-thailand remote"
        echo "Please check your permissions and network connection"
        exit 1
    fi
else
    echo "❌ Push cancelled by user"
    exit 0
fi

echo ""
echo "🎉 Django Portfolio successfully committed to Otop-Thailand repository!"