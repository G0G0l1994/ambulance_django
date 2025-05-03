from django.urls import path

from .views import (
    custom_login,
    dispatcher_page,
    doctor_page,
    home,
    logout_user,
    register,
)

urlpatterns = [
    path("register/", register, name="register"),
    path("", home, name="home"),
    path("login/", custom_login, name="login"),
    path("doctors/", doctor_page, name="doctors"),
    path("dispatcher/", dispatcher_page, name="dispatcher"),
    path("logout/", logout_user, name="logout"),
]
