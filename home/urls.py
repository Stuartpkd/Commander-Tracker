from django.urls import path
from . import views
from .views import commanders_view

urlpatterns = [
    # ... other url patterns ...
    path('cards/', views.fetch_cards, name='fetch-cards'),
    path('commanders/', commanders_view, name='commanders'),
]