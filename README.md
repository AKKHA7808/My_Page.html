# Django Portfolio Website

A personal portfolio website built with Django featuring a modern glass morphism design.

## Features

- **Multi-section Portfolio**: Home, About, and Contact pages in a single-page application
- **Modern Design**: Glass morphism effect with gradient backgrounds
- **Responsive Layout**: Bootstrap 5 for mobile-friendly design
- **Interactive Elements**: 
  - Image carousel
  - Skills progress bars
  - Contact form
  - Smooth page transitions
- **Thai Language Support**: Content in Thai language
- **Production Ready**: Configured for Vercel deployment

## Tech Stack

- **Backend**: Django 5.1.4
- **Frontend**: Bootstrap 5, Custom CSS/JS
- **Deployment**: Vercel with WhiteNoise for static files
- **Database**: SQLite (development)

## Project Structure

```
My_Page/
├── main/                   # Main Django app
│   ├── templates/main/     # HTML templates
│   ├── views.py           # View functions
│   └── urls.py           # URL routing
├── portfolio/             # Django project settings
│   ├── settings.py       # Project configuration
│   ├── urls.py          # Main URL routing
│   └── wsgi.py          # WSGI application
├── static/               # Static files
│   ├── css/style.css    # Custom styles
│   └── js/main.js       # JavaScript functionality
├── vercel.json          # Vercel deployment config
├── requirements.txt     # Python dependencies
└── build.sh            # Build script for deployment
```

## Local Development

1. **Clone and Navigate**:
   ```bash
   cd c:\Django\My_Page
   ```

2. **Activate Virtual Environment**:
   ```bash
   .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Collect Static Files**:
   ```bash
   python manage.py collectstatic
   ```

6. **Start Development Server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the Website**:
   Open http://127.0.0.1:8000 in your browser

## Deployment to Vercel

1. **Install Vercel CLI**:
   ```bash
   npm install -g vercel
   ```

2. **Deploy**:
   ```bash
   vercel
   ```

3. **Follow the prompts** to configure your deployment

## Features Overview

### Home Page
- Welcome message with typing animation
- Image carousel with smooth transitions
- Feature cards showcasing skills and interests

### About Page
- Personal introduction
- Skills section with animated progress bars
- Professional background information

### Contact Page
- Contact form with validation
- Contact information display
- Form submission handling

## Customization

### Content
- Edit `main/templates/main/index.html` to modify content
- Update Thai text to match your personal information
- Replace placeholder images with your own photos

### Styling
- Modify `static/css/style.css` for design changes
- Adjust colors, fonts, and layouts
- The design uses CSS custom properties for easy theming

### Functionality
- Update `static/js/main.js` for interactive features
- Modify `main/views.py` to add new functionality
- Extend the contact form to send emails or save to database

## Dependencies

- Django 5.1.4 - Web framework
- whitenoise 6.8.2 - Static file serving
- gunicorn 23.0.0 - WSGI server for production

## License

This project is open source and available under the MIT License.
