from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Category


@login_required
def user_profile(request):

    context = {'user': request.user}
    return render(request, 'profiles/profiles.html', context)


def create_category(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        Category.objects.create(name=category_name, user=request.user)
        return redirect('profile_page')  # Redirect to the profile page or category management page

    return render(request, 'profiles/create_category.html')
