<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# Django Portfolio Project Instructions

This is a Django web application project featuring a personal portfolio website with the following characteristics:

## Project Structure
- **Django Version**: 5.1.4
- **Main App**: `main` - handles portfolio pages (home, about, contact)
- **Template Engine**: Django templates with Bootstrap 5
- **Static Files**: CSS and JavaScript for styling and interactivity
- **Deployment**: Configured for Vercel deployment

## Key Features
- Single-page application with three sections: Home, About, Contact
- Glass morphism design with gradient backgrounds
- Responsive Bootstrap 5 UI
- Thai language content
- Contact form functionality
- Carousel image gallery
- Skills progress bars
- Smooth page transitions

## Development Guidelines
- Use Django best practices for views, urls, and templates
- Maintain the glass morphism design aesthetic
- Keep Thai language content consistent
- Ensure mobile responsiveness
- Follow Bootstrap 5 conventions
- Use semantic HTML structure

## Deployment
- Configured for Vercel with `vercel.json`
- Uses WhiteNoise for static file serving
- Includes `build.sh` script for deployment
- Production-ready settings with environment variables

## Files Structure
- Templates: `main/templates/main/index.html`
- Static files: `static/css/style.css`, `static/js/main.js`
- Views: `main/views.py` handles all portfolio pages
- URLs: `main/urls.py` and `portfolio/urls.py`
