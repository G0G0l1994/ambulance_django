from django.core.exceptions import PermissionDenied

def get_role_redirect(profile):
    
    if profile.role == "doctor":
        return 'doctor-page'
    elif profile.role == "dispatcher":
        return 'dispatcher-page'
    else:
        raise PermissionDenied('Неизвестная роль пользователя')
    
    
    
