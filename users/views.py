from django.shortcuts import render, get_object_or_404, redirect

from .models import Profile


def get_profile(request):
    # profile = Profile.objects.get(id=request.POST['id'])
    profile = Profile.objects.all().first()

    return render(request, 'users/profile.html', {'profile': profile})
