from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import date
import json
from .models import Students

def index(request):
    """Main portfolio page - Home section"""
    return render(request, 'main/home.html')

def about(request):
    """About page with personal information"""
    return render(request, 'main/about.html')

def contact(request):
    """Contact page with form"""
    if request.method == 'POST':
        # Handle contact form submission
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Here you can add logic to save to database or send email
        # For now, we'll just return success
        context = {
            'message_sent': True,
            'form_data': {
                'name': name,
                'lastname': lastname,
                'email': email,
                'message': message
            }
        }
        return render(request, 'main/contact.html', context)
    
    return render(request, 'main/contact.html')

def for_loop_example(request):
    """For loop example page with tables and data"""
    
    # Sample data for demonstration
    items = [
        'HTML & CSS',
        'JavaScript & React',
        'Python & Django',
        'Bootstrap Framework',
        'Git & GitHub',
        'Database Design'
    ]
    
    students = [
        {
            'first_name': 'สมชาย',
            'last_name': 'ใจดี',
            'email': 'somchai@email.com',
            'score': 85
        },
        {
            'first_name': 'สมหญิง',
            'last_name': 'รักเรียน',
            'email': 'somying@email.com',
            'score': 92
        },
        {
            'first_name': 'กิตติ',
            'last_name': 'ขยันเรียน',
            'email': 'kitti@email.com',
            'score': 78
        },
        {
            'first_name': 'อนุชา',
            'last_name': 'ปรีชา',
            'email': 'anucha@email.com',
            'score': 95
        },
        {
            'first_name': 'มาลี',
            'last_name': 'สวยงาม',
            'email': 'mali@email.com',
            'score': 67
        }
    ]
    
    projects = [
        {
            'name': 'E-Commerce Website',
            'description': 'ระบบขายของออนไลน์',
            'technologies': ['Django', 'PostgreSQL', 'Bootstrap'],
            'status': 'completed',
            'progress': 100,
            'created_date': date(2024, 1, 15)
        },
        {
            'name': 'Portfolio Website',
            'description': 'เว็บไซต์แสดงผลงาน',
            'technologies': ['HTML', 'CSS', 'JavaScript'],
            'status': 'completed',
            'progress': 100,
            'created_date': date(2024, 2, 10)
        },
        {
            'name': 'Mobile App',
            'description': 'แอพพลิเคชันมือถือ',
            'technologies': ['React Native', 'Firebase'],
            'status': 'in_progress',
            'progress': 75,
            'created_date': date(2024, 3, 5)
        },
        {
            'name': 'Data Dashboard',
            'description': 'แดชบอร์ดแสดงข้อมูล',
            'technologies': ['Python', 'Streamlit', 'Pandas'],
            'status': 'pending',
            'progress': 25,
            'created_date': date(2024, 4, 1)
        }
    ]
    
    # Handle skills data for checkboxes
    selected_skills = []
    if request.method == 'POST':
        selected_skills = request.POST.getlist('skills')
    
    context = {
        'items': items,
        'students': students,
        'projects': projects,
        'count': range(1, 13),  # Creates a range from 1 to 12 for multiplication table
        'selected_skills': selected_skills,
    }
    
    return render(request, 'main/for.html', context)

def students_list(request):
    """Students page displaying all student records"""
    students = Students.objects.all().order_by('student_id')
    
    context = {
        'students': students,
        'total_students': students.count(),
    }
    
    return render(request, 'main/students.html', context)
