from django.urls import path
from . import views as user_views

urlpatterns = [
    path('', user_views.home, name='user-home'),
    path('register/', user_views.register, name='user-register'),
    path('login/', user_views.loginUser, name='user-login'),
    path('logout/', user_views.logoutUser, name='user-logout'),
    path('profile/', user_views.profile, name='user-profile')
]