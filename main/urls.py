from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('for-loop/', views.for_loop_example, name='for_loop'),
]
