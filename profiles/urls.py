from django.urls import path
from .views import index, profile_view, signup_view, signin_view

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup_view, name='signup'),
    path('signin/', signin_view, name='signin'),
    path('profile/', profile_view, name='profile'),
]
