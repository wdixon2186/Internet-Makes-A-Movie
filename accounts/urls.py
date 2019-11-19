from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Login / Log Out
    path('accounts/login/',
         auth_views.LoginView.as_view(template_name='accounts/login.html'),
         name='login'),
    path('accounts/logout/',
         auth_views.LogoutView.as_view(template_name='accounts/logout.html'),
         name='logout'),
    path('signup/', views.SignUp, name='signup'),
]
