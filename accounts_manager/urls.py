from django.urls import path
from . import views


urlpatterns = [
    # path('login', views.login_user_view, name='login'),
    path('logout', views.logout_user_view, name='logout'),
    path('register', views.register_user_view, name='register'),
    path('', views.home_view, name='home'),
    path('profile', views.profile_view, name='profile'),
    path('add_personal_info', views.add_personal_information_view, name='add_personal_info'),
    path('insert_personal_info', views.insert_personal_information, name='insert_personal_info'),
]
