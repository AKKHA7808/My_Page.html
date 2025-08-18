# 🚀 Vercel Auto Deployment Guide

This guide explains how to set up automatic deployment to Vercel for your Django Portfolio project.

## 📋 Prerequisites

- GitHub repository connected to Vercel
- Vercel CLI installed
- Node.js installed

## ⚙️ Auto Deployment Setup

### 1. 🔗 Connect GitHub to Vercel

1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Click "New Project"
3. Import your GitHub repository `AKKHA7808/My_Page.html`
4. Configure build settings (will use `vercel.json` automatically)

### 2. 🔑 GitHub Secrets (for GitHub Actions)

Add these secrets to your GitHub repository:

```
Settings → Secrets and variables → Actions → New repository secret
```

Required secrets:
- `VERCEL_TOKEN`: Your Vercel API token
- `VERCEL_ORG_ID`: Your Vercel organization ID  
- `VERCEL_PROJECT_ID`: Your project ID

To get these values:
```bash
# Install Vercel CLI
npm install -g vercel

# Login and get project info
vercel login
vercel link
cat .vercel/project.json
```

### 3. 🔄 Automatic Deployment Triggers

**Production Deployment:**
- Automatically deploys when pushing to `main` branch
- GitHub Actions runs tests first
- Only deploys if tests pass

**Preview Deployment:**
- Automatically creates preview for Pull Requests
- Useful for testing changes before merging

## 🛠️ Manual Setup

Run the setup script:
```bash
python setup_vercel.py
```

Or manually:
```bash
# Install Vercel CLI
npm install -g vercel

# Login to Vercel
vercel login

# Link project
vercel link

# Set environment variables
vercel env add DEBUG production
vercel env add DJANGO_ENV production
vercel env add DJANGO_SETTINGS_MODULE production
```

## 📝 GitHub Actions Workflows

### Deploy Workflow (`.github/workflows/deploy.yml`)
- Runs tests on every push/PR
- Deploys to Vercel production on main branch
- Creates preview deployments for PRs

### Quality Workflow (`.github/workflows/quality.yml`)
- Code formatting checks (Black)
- Import sorting (isort)
- Linting (flake8)
- Security scanning (Safety, Bandit)

## 🔧 Vercel Configuration

The `vercel.json` file configures:
- Python runtime (3.11)
- Entry point (`index.py`)
- Environment variables
- GitHub integration settings
- Build optimization

## 🚀 Deployment Process

1. **Push code to GitHub**
   ```bash
   git add .
   git commit -m "Your changes"
   git push origin main
   ```

2. **GitHub Actions runs**
   - Tests Django application
   - Checks code quality
   - Deploys to Vercel if tests pass

3. **Vercel builds and deploys**
   - Installs Python dependencies
   - Runs Django setup
   - Creates serverless function
   - Deploys to production URL

## 📊 Monitoring Deployments

### Vercel Dashboard
- View deployment status
- Check build logs
- Monitor performance
- Manage domains

### GitHub Actions
- View workflow runs
- Check test results
- Debug deployment issues

### Useful Commands
```bash
# View Vercel logs
vercel logs

# Manual production deployment
vercel --prod

# List deployments
vercel ls

# Check project status
vercel inspect
```

## 🐛 Troubleshooting

### Common Issues

**Build Failures:**
- Check Python dependencies in `requirements.txt`
- Verify Django settings in `portfolio/settings/production.py`
- Review Vercel build logs

**Import Errors:**
- Ensure all required packages are in `requirements.txt`
- Check Python path configuration
- Verify Django settings module

**Static Files:**
- Django's `collectstatic` runs automatically
- WhiteNoise serves static files
- Check `STATIC_URL` and `STATIC_ROOT` settings

### Debug Steps

1. **Check Vercel logs:**
   ```bash
   vercel logs --follow
   ```

2. **Run local tests:**
   ```bash
   python manage.py check
   python manage.py test
   ```

3. **Verify production settings:**
   ```bash
   DJANGO_ENV=production python manage.py check
   ```

## 🎯 Benefits of Auto Deployment

- **🚀 Continuous Deployment**: Automatic deployment on every push
- **🧪 Quality Assurance**: Tests run before deployment
- **📱 Preview Deployments**: Test changes before going live
- **🔄 Rollback**: Easy rollback to previous versions
- **📊 Monitoring**: Built-in monitoring and logging

## 🔗 Related Links

- [Vercel Documentation](https://vercel.com/docs)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Django Deployment Guide](https://docs.djangoproject.com/en/stable/howto/deployment/)

---

**📝 Note**: After setting up auto deployment, every push to the main branch will automatically deploy to production. Make sure to test changes in feature branches first!
