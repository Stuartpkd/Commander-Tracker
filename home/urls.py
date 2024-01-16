from django.urls import path
from . import views

urlpatterns = [
    # ... other url patterns ...
    path('cards/', views.fetch_cards, name='fetch-cards'),
]
