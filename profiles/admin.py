from django.contrib import admin
from .models import SavedCard  # Adjust the import path according to your project structure

@admin.register(SavedCard)
class SavedCardAdmin(admin.ModelAdmin):
    list_display = ('card', 'user_profile', 'category')  # Add other fields as needed
    list_filter = ('category',)
    search_fields = ('card__name', 'user_profile__user__username', 'category__name')  # Adjust according to your field names
