from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('students/', views.students_list, name='students'),
    path('for-loop/', views.for_loop_example, name='for_loop'),
]
