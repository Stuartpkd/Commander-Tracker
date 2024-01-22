from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, SavedCard
from home.models import Card


@login_required
def user_profile(request):
    
    user_categories = Category.objects.filter(user=request.user)

    context = {
        'user': request.user,
        'user_categories': user_categories,  
    }
    return render(request, 'profiles/profiles.html', context)


def create_category(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        Category.objects.create(name=category_name, user=request.user)
        return redirect('user_profile')  # Redirect to the profile page or category management page

    return render(request, 'profiles/create_category.html')


def add_card_to_category(request, card_id):
    if request.method == 'POST':
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id, user=request.user)
        card = Card.objects.get(id=card_id)
        # Assuming SavedCard is the through model between UserProfile and Card
        SavedCard.objects.create(user_profile=request.user.userprofile, card=card, category=category)
        return redirect('card_detail', card_id=card_id)  # Redirect back to the card detail page

    # Additional context or error handling as necessary

