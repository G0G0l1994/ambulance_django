from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api.v1.views.user import user_create, users_list

urlpatterns = [path("users/", users_list), path("users/create/", user_create)]

urlpatterns = format_suffix_patterns(urlpatterns)
