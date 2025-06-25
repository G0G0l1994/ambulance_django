from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.v1.serializers.user import UserSerializer
from user.models import Profile

@api_view(['GET',"POST"])
def users_list(request,format=None):
    if request.method == "GET":
        users = Profile.objects.select_related('user').all()
        serializer = UserSerializer(users,many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)