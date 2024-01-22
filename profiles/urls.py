from django.urls import path
from .views import user_profile, add_card_to_category, create_category

urlpatterns = [
    path('profile/', user_profile, name='user_profile'),
    path('add_card_to_category/<int:card_id>/', add_card_to_category, name='add_card_to_category'),
    path('create_category/', create_category, name='create_category'),
]
