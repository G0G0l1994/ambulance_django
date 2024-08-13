from django.urls import path
from card.views import new

urlpatterns = [path('new/', new, name='new')]