from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api.v1.views.user import *
from api.v1.views.card import CardAPIView

urlpatterns = [path("users/", UserAPIView.as_view()),
               path("cards/", CardAPIView.as_view()),
               path('users/login/', LoginAPIView.as_view()),
               path('users/refresh/', RefreshTokenObtain.as_view()),
               path('users/logout/', LogoutAPIView.as_view()),
               path('registration/', RegistrationAPIVeiw.as_view()),
               path('authenticated/', IsAuthenticatedAPIView.as_view()),
               
               ]

urlpatterns = format_suffix_patterns(urlpatterns)
