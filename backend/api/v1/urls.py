from django.urls import path
from django.http import HttpResponse
from rest_framework import status
from rest_framework.urlpatterns import format_suffix_patterns

from api.v1.views.user import *
from api.v1.views.card import *

def health_check(request):
    return HttpResponse({"health_check": "OK"}, status=status.HTTP_200_OK)

urlpatterns = [
    path('health/',health_check),
    path("users/", UserAPIView.as_view()),
    path('users/profile/',ProfileAPIView.as_view()),
    path("cards/", CardListAPIView.as_view()),
    path("cards/doctor/<int:user_id>", CardListAPIView.as_view()),
    path('cards/<int:card_id>/', CardDetailAPIView.as_view()),
    path('cards/<int:card_id>/update/', CardUpdateAPIVView.as_view()),
    path('cards/create/', CardCreateAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
    path('users/refresh/', RefreshTokenObtain.as_view()),
    path('users/logout/', LogoutAPIView.as_view()),
    path('registration/', RegistrationAPIVeiw.as_view()),
    path('authenticated/', IsAuthenticatedAPIView.as_view()),
    path('mkb/', MKBListAPIView.as_view()),
    path('users/doctor-list/', DoctorListView.as_view()),
    path('crew/list/', CrewListAPIView.as_view()),
    path('crew/create/', CrewCreateAPIVeiw.as_view()),
    path('crew/<int:crew_id>/update/',CrewUpdateApiView.as_view()),
    path("crew/dispatch/", DispatchCardToCrewAPIView.as_view()),

    ]

urlpatterns = format_suffix_patterns(urlpatterns)
