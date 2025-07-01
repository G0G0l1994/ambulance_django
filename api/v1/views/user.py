from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.v1.serializers.user import UserCreateSerializer, UserSerializer
from user.models import Profile


@api_view(["GET", "POST"])
def users_list(request, _format=None):
    if request.method == "GET":
        users = Profile.objects.select_related("user").all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def user_create(request, _format=None):
    if request.method == "POST":
        seriailizer = UserCreateSerializer(data=request.data)
        if seriailizer.is_valid():
            user = seriailizer.save()
            return Response(
                {
                    "status": "success",
                    "data": {
                        "username": user.username,
                        "email": user.email,
                        "first_name": user.first_name,
                        "surname": user.profile.surname,
                        "last_name": user.last_name,
                        "role": user.profile.role,
                    },
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(seriailizer.data, status=status.HTTP_400_BAD_REQUEST)
