from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

from api.v1.serializers.user import UserCreateSerializer
from user.models import Profile


class ReactView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    parser_classes = [FormParser, MultiPartParser, JSONParser]
    serializer_class = UserCreateSerializer
    
    
    def get(self,request, format = None):
        output = [
            {
                        "username": profile.user.username,
                        "email": profile.user.email,
                        "first_name": profile.user.first_name,
                        "surname": profile.surname,
                        "last_name": profile.user.last_name,
                        "role": profile.role,
                    }
                    for profile in Profile.objects.select_related('user').all()
        ]

        return Response(output)

    def post(self,request, format = None):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)