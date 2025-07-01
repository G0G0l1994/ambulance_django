from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api.v1.views.user import ReactView

urlpatterns = [path("users/", ReactView.as_view())]

urlpatterns = format_suffix_patterns(urlpatterns)
