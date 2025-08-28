import jwt

from django.contrib.auth import authenticate


from rest_framework import status
from rest_framework.permissions import AllowAny
 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

from api.v1.serializers.user import UserCreateSerializer, UserSerializer, CrewSerializer
from project import settings
from user.models import Profile, RefreshToken, Crew
from user.services.auth import create_jwt_token, create_refresh_token


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
                        "is_online": profile.is_online,
                        
                    }
                    for profile in Profile.objects.select_related('user').all()
        ]

        return Response(output)

class ProfileAPIView(APIView):

    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    parser_classes = [FormParser, MultiPartParser, JSONParser]
    serializer_class = UserSerializer

    def get(self, request):
        from user.models import Profile
        user = request.user
        try:
            profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            return Response({'detail': 'Профиль не найден'}, status=404)
        serializer = self.serializer_class(profile)
        return Response(serializer.data, status=200)
    

class DoctorListView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    parser_classes = [FormParser, MultiPartParser, JSONParser]
    serializer_class = UserSerializer

    def get(self, request):
        doctors = Profile.objects.filter(role='doctor', is_online=True)
        serializers = self.serializer_class(doctors, many=True)

        return Response(serializers.data, status=status.HTTP_200_OK)

class CrewCreateAPIVeiw(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    parser_classes = [FormParser, MultiPartParser,JSONParser]
    serializer_class = CrewSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(f"CrewSerializer error: {serializer.error}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CrewUpdateApiView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    parser_classes = [FormParser, MultiPartParser,JSONParser]
    serializer_class = CrewSerializer

    def put(self, request, crew_id):
        try:
            crew = Crew.objects.get(id=crew_id)
        except Crew.DoesNotExist:
            return Response({'detail': 'Crew not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(crew, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            print(f"crew {crew.crew_number} updated")
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CrewListAPIView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    parser_classes = [FormParser, MultiPartParser,JSONParser]
    serializer_class = CrewSerializer

    def get(self,request):
        crew_list = Crew.objects.select_related("main__profile", "secondary__profile").all()
        serializer = self.serializer_class(crew_list, many=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RegistrationAPIVeiw(APIView):

    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer
    parser_classes = [FormParser, MultiPartParser, JSONParser]

    def post(self,request, format = None):
        print(f"Registration request data: {request.data}")
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(f"Serializer errors: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):

    permission_classes = [AllowAny]
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username,password=password)
        if user is not None and user.is_active and hasattr(user,'profile'):
            user.profile.is_online = True
            if not user.profile.uuid_is_active:
                user.profile.refresh_session()
            user.profile.save()
            access_token = create_jwt_token(user)
            refresh_token = create_refresh_token(user)
            res = Response({"success": True, "access_token": access_token, "refresh_token": refresh_token, "role": user.profile.role, "is_online": user.profile.is_online},status=status.HTTP_200_OK)
            
            print(f"Setting cookies for user {user.username} {user.profile.role}")
            print(f"Access token: {access_token[:20]}...")
            
            res.set_cookie(key="access_token",
            value=access_token,
            httponly=False,
            secure=False,
            samesite='Lax',
            path='/',
            domain=None)
            res.set_cookie(key="refresh_token",
            value=refresh_token,
            httponly=False,
            secure=False,
            samesite='Lax',
            path='/',
            domain=None)
            
            print("Cookies set successfully")
            return res
        return Response({"success": False,"detail": "Invalid user data"}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutAPIView(APIView):

    permission_classes =[AllowAny]
    def post(self,request):
        try:
            refresh_token = request.COOKIES.get('refresh_token')
            if refresh_token:
                try:
                    payload = jwt.decode(refresh_token, key = settings.SECRET_KEY, algorithms=['HS256'])
                    jti = payload.get('jti')
                    user_id = payload.get('user_id')
                    if user_id:
                        profile = Profile.objects.get(user_id=user_id)
                        profile.is_online = False
                        profile.save()
                    if jti:
                        RefreshToken.objects.filter(jti=jti).update(revoked=True)
                except Exception:
                    pass
            response = Response({'success': True})
            response.delete_cookie('refresh_token', path='/', samesite='Lax', domain=None)
            response.delete_cookie('access_token', path='/', samesite='Lax', domain=None)
            return response
        except Exception as e:
            print(f"Error is {e}")
            return Response({'detail': 'Something wrong', 'success': False}, status=status.HTTP_400_BAD_REQUEST)




class RefreshTokenObtain(APIView):

    permission_classes = [AllowAny]

    def post(self,request):
        token = request.COOKIES.get('refresh_token')
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
        response.set_cookie(
            "access_token", 
            access_token, 
            httponly=False,
            secure=False,
            samesite='Lax',
            domain=None)
        return response

class IsAuthenticatedAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Проверяем наличие access_token в cookie
        access_token = request.COOKIES.get('access_token')
        
        print(f"All cookies: {dict(request.COOKIES)}")
        print(f"Checking authentication. Access token: {'present' if access_token else 'missing'}")
        
        if not access_token:
            print("No access token found")
            return Response({'is_authenticated': False})
        
        try:
            # Декодируем JWT токен
            payload = jwt.decode(access_token, key=settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload.get('user_id')
            uuid_session = payload.get('uuid_session')
            
            print(f"Token payload - user_id: {user_id}, uuid_session: {uuid_session}")
            
            if not user_id:
                print("No user_id in token")
                return Response({'is_authenticated': False})
            
            # Проверяем, что пользователь существует и активен
            from django.contrib.auth import get_user_model
            User = get_user_model()
            
            try:
                user = User.objects.get(id=user_id, is_active=True)
                print(f"User found: {user.username}")
                
                # Проверяем, что у пользователя есть профиль
                if hasattr(user, 'profile'):
                    print(f"User has profile, uuid_session: {user.profile.uuid_session}")
                    
                    # Проверяем совпадение uuid_session
                    if str(user.profile.uuid_session) == uuid_session:
                        print("UUID session matches")
                        if user.profile.uuid_is_active:
                            print("Session is active")
                            return Response({'is_authenticated': True})
                        else:
                            print("Session expired")
                            return Response({'is_authenticated': False})
                    else:
                        print(f"UUID session mismatch. Token: {uuid_session}, Profile: {user.profile.uuid_session}")
                        return Response({'is_authenticated': False})
                else:
                    print("User has no profile")
                    return Response({'is_authenticated': False})
            except User.DoesNotExist:
                print(f"User with id {user_id} not found")
                return Response({'is_authenticated': False})
                
        except jwt.ExpiredSignatureError:
            print("Token expired")
            return Response({'is_authenticated': False})
        except jwt.InvalidTokenError:
            print("Invalid token")
            return Response({'is_authenticated': False})
        except Exception as e:
            print(f"Error checking authentication: {e}")
            return Response({'is_authenticated': False})
