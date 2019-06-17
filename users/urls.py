from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_profile, name='get_profile'),
    path('signup/', views.ProfileCreateView.as_view(), name='create_user'),
    path('login/', views.CustomLoginView.as_view(), name='login_user'),
    path('logout/', views.logout, name='logout'),
    path('edit/', views.profile_edit, name='profile_edit'),

]
