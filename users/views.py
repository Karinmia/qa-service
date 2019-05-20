from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import UserCreationForm
from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalDeleteView)
from .models import Profile


def get_profile(request):
    # profile = Profile.objects.get(id=request.POST['id'])
    profile = Profile.objects.all().first()

    return render(request, 'users/profile.html', {'profile': profile})


class ProfileCreateView(BSModalCreateView):
    template_name = 'users/create_user.html'
    form_class = UserCreationForm
    success_url = reverse_lazy(get_profile)