from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def user_profile(request):

    context = {'user': request.user}
    return render(request, 'profiles/templates/profile.html', context)
