from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth import logout as auth_logout

from bootstrap_modal_forms.generic import BSModalCreateView, BSModalLoginView

from .models import Profile
from .forms import CustomCreationForm, CustomAuthenticationForm, ProfileForm


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


def profile_edit(request, pk=None):
    profile = get_object_or_404(Profile, pk=pk) if pk else None

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('get_profile', pk=profile.pk)
    else:
        form = ProfileForm(instance=profile)

    if pk:
        action = reverse(profile_edit, args=[pk])
    else:
        action = reverse(profile_edit)

    return render(request, 'users/profile_edit.html', {'form': form, 'action': action})