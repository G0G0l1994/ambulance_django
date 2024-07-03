from django.urls import path
from .views import register,custom_login, home
from django.contrib.auth import views
from .forms import LoginForm

urlpatterns = [path('register/', register,name='register'),
               path('',home,name='home'),
               path('login/',custom_login,name="login")]