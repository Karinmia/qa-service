from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin

from .models import Profile

class CustomCreationForm(PopRequestMixin, CreateUpdateAjaxMixin, UserCreationForm):
    class Meta:
        model = User
        fields = [
                  'email',
                  'username',
                  'password1',
                  'password2'
                  ]


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username',
                  'password'
                  ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('jira_login', 'jira_password')


class ChangePass(forms.ModelForm):
    class Meta:
        model = User
        fields = ('password',
                  )
