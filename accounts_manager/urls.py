from django.urls import path
from . import views


urlpatterns = [
    # path('login', views.login_user_view, name='login'),
    path('logout', views.logout_user_view, name='logout'),
    path('register', views.register_user_view, name='register'),
    path('', views.home_view, name='home'),
    path('profile', views.profile_view, name='profile'),
]
