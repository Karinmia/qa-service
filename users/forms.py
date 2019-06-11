from django.contrib.auth.forms import UserCreationForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

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

