# urls.py

from django.urls import path
from .views import fetch_legendary_creatures, index

urlpatterns = [
    # ... other URL patterns ...
    path('commanders/', fetch_legendary_creatures, name='commanders'),
    path('', index, name='home'),
]
