from django.contrib.auth import authenticate, login
from django.core.exceptions import PermissionDenied

from .role import get_role_redirect

def login_user(request, username: str, password: str):
    
    user = authenticate(request, 
                        username=username,
                        password=password)
    if not user or hasattr(user, 'profile'):
        raise PermissionDenied('Пользователю доступ запрещён')
    
    login(request,user)
    return get_role_redirect(user.profile)