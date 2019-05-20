from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_profile, name='get_profile'),
    path('signup/', views.ProfileCreateView.as_view(), name='create_user'),
]
