from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import CustomCreationForm, CustomAuthenticationForm
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalLoginView
from django.contrib.auth import logout as auth_logout
from .models import Profile


def get_profile(request):
    profile = Profile.objects.all().first()

    return render(request, 'users/profile.html', {'profile': profile})


class ProfileCreateView(BSModalCreateView):
    template_name = 'users/create_user.html'
    form_class = CustomCreationForm
    success_url = reverse_lazy('get_profile')


class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'users/auth.html'
    extra_context = dict(success_url=reverse_lazy('get_profile'))


def logout(request):
    auth_logout(request)

