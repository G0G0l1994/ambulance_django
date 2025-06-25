from django.core.exceptions import PermissionDenied


def get_role_redirect(profile):
    if profile.role == "doctors":
        return "doctors"
    elif profile.role == "dispatchers":
        return "dispatchers"
    else:
        raise PermissionDenied("Неизвестная роль пользователя")
