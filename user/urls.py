from django.urls import path
from .views import register,custom_login,logout_user, home, doctor_page, dispatcher_page
from django.contrib.auth import views
from .forms import LoginForm

urlpatterns = [path('register/', register,name='register'),
               path('',home,name='home'),
               path('login/',custom_login,name="login"),
               path('doctors/',doctor_page,name="doctors"),
               path('dispatcher/',dispatcher_page, name="dispatcher"),
               path('logout/',logout_user, name='logout')]