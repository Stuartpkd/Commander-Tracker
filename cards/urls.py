from django.urls import path
from .views import CardDetailView

urlpatterns = [
    # ... other URL patterns ...
    path('cards/card/<int:pk>/', CardDetailView.as_view(), name='card_detail'),
]
