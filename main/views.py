from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    """Main portfolio page with all sections"""
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
        return render(request, 'main/index.html', context)
    
    return render(request, 'main/index.html')
