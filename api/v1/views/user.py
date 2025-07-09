import jwt

from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

from api.v1.serializers.user import UserCreateSerializer
from project import settings
from user.models import Profile, RefreshToken
from user.services.auth import create_jwt_token


class UserAPIView(APIView):
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
                        "session":profile.uuid_session,
                        "expire": profile.session_expire,
                        
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

class LoginAPIView(APIView):

    permission_classes = [AllowAny]
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username,password=password)
        if user is not None and user.is_active and hasattr(user,'profile'):
            if not user.profile.uuid_is_active:
                user.profile.refresh_session()
            token = create_jwt_token(user)
            res = Response({"success": True, "access": token},status=status.HTTP_200_OK)
            
            res.set_cookie(key="access_token",
            value=token,
            httponly=True,
            secure=not settings.DEBUG,
            samesite='Lax',
            path='/')
            return res
        return Response({"success": False,"detail": "Invalid user data"}, status=status.HTTP_401_UNAUTHORIZED)

class RefreshTokenObtain(APIView):

    permission_classes = [AllowAny]
    
    def post(self,request):
        token = request.data.get('refresh')
        if not token:
            return Response({'detail': 'Refresh token required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            payload = jwt.decode(token, key=settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload.get('user_id')
            jti = payload.get('jti')
            if not user_id or not jti:
                return Response({'detail': 'Invalid refresh token payload'}, status= status.HTTP_400_BAD_REQUEST)
        except jwt.ExpiredSignatureError:
            return Response({'detail': 'Refresh token expired'}, status=status.HTTP_401_UNAUTHORIZED)
        except jwt.InvalidTokenError:
            return Response({'detail': 'Invalid refresh token'}, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            refresh_token = RefreshToken.objects.get(user_id=user_id,jti=jti,revoked=False)
        except RefreshToken.DoesNotExist:
            return Response({'detail': 'Refresh token not found or revoked'}, status=status.HTTP_401_UNAUTHORIZED)
        
        if  not refresh_token.jti_is_active:
             return Response({'detail': 'Refresh token expired'}, status=status.HTTP_401_UNAUTHORIZED)
        
        user = refresh_token.user
        access_token = create_jwt_token(user)

        response = Response({'access': access_token}, status=status.HTTP_200_OK)
        response.set_cookie("access_token", access_token, httponly=True, secure=not settings.DEBUG, samesite="Lax")
        return response