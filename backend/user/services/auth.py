from datetime import timedelta
from typing import Optional

from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.utils import timezone
import jwt
from rest_framework import exceptions,status
from rest_framework.authentication import BaseAuthentication


from user.models import RefreshToken


def create_jwt_token(user) -> str:
    exp = (timezone.now() + timedelta(hours=24)).timestamp()
    payload = {
        "user_id": str(user.id),
        "uuid_session": str(user.profile.uuid_session),
        "exp": exp,
    }

    return jwt.encode(payload=payload, key=settings.SECRET_KEY, algorithm="HS256")


def validate_jwt_token(token) -> Optional[User]:
    try:
        payload = jwt.decode(token, key=settings.SECRET_KEY, algorithms=["HS256"], options={"verify_exp": True})
        user = User.objects.get(id=payload["user_id"])
        
        # Проверяем, что uuid_session в токене совпадает с uuid_session в профиле
        if str(user.profile.uuid_session) == payload["uuid_session"]:
            if user.is_active and user.profile.uuid_is_active:
                return user
        return None
    except Exception as error:
        if settings.DEBUG:
            print(f'JWT validation error: {error}')
        return None


def create_refresh_token(user) -> str:
    """Создаёт запись RefreshToken и возвращает JWT с полями user_id и jti.

    В БД хранится состояние токена (revoked, expires_at). В JWT кладём ссылочный jti,
    по которому `RefreshTokenObtain` и `Logout` смогут найти запись и валидировать/аннулировать её.
    """
    # Сначала создаём и сохраняем запись refresh-токена в БД, чтобы jti был зафиксирован
    token = RefreshToken(user=user)
    token.save()  # фиксируем jti и expires_at по умолчанию

    exp = (timezone.now() + timedelta(days=7)).timestamp()
    payload = {
        "user_id": user.id,
        "jti": str(token.jti),
        "exp": exp,
    }
    return jwt.encode(payload=payload, key=settings.SECRET_KEY, algorithm="HS256")

def is_valid_refresh_token(token):
    try:
        payload = jwt.decode(token, key=settings.SECRET_KEY, algorithms=["HS256"], options={"verify_exp": True})
        user = User.objects.get(id=payload["user_id"], refresh__uuid_session=payload["uuid_session"])
        if user.is_active and user.profile.uuid_is_active:
            return user
        return None
    except Exception as error:
        if settings.DEBUG:
            print(f'JWT validation error: {error}')
        return None


class CustomJWTAuth(BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get('access_token')
        
        if not token:
            auth_header = request.headers.get('Authorization')
            if auth_header and auth_header.startswith('Bearer '):
                token = auth_header.split(' ')[1]
        
        if not token:
            return None
            
        user = validate_jwt_token(token)
        if user is None:
            raise exceptions.AuthenticationFailed('Invalid or expired token')
        return (user,None)




