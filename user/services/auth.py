import jwt
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.utils import timezone


def create_jwt_token(user) -> str:
    payload = {
        "user_id": str(user.id),
        "uuid_session": str(user.profile.uuid_session),
        "exp": timezone.now() + timezone.timedelta(hours=24),
    }

    return jwt.encode(payload=payload, key=settings.SECRET_KEY, algorithm="HS256")


def validate_jwt_token(token) -> User:
    try:
        payload = jwt.decode(token, key=settings.SECRET_KEY, algorithms=["HS256"], options={"verify_exp": True})
        user = User.objects.get(id=payload["user_id"], profile__uuid_session=payload["uuid_session"])
        if user.is_active and user.profile.uuid_is_active:
            return user
        return None
    except Exception:
        return None


def user_auth(request, username: str, password: str):
    user = authenticate(request, username=username, password=password)

    if not user or not hasattr(user, "profile"):
        raise PermissionDenied("Пользователю доступ запрещён")
    if not user.profile.uuid_is_active:
        user.profile.refresh_session()
    return user


