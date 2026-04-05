from django.urls import path
from .views import generate_patterns

urlpatterns = [
    path('generate/', generate_patterns, name='generate_patterns'),
]