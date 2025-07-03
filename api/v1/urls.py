from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api.v1.views.user import ReactView
from api.v1.views.card import CardAPIView

urlpatterns = [path("users/", ReactView.as_view()),
               path("cards/", CardAPIView.as_view())]

urlpatterns = format_suffix_patterns(urlpatterns)
