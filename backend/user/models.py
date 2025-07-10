import logging
import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now, timedelta

logger = logging.getLogger(__name__)

def get_expire_time():
    return now() + timedelta(days=30)

def get_token_expire_time():
    return now() + timedelta(days=7)

class Profile(models.Model):
    ROLE_CHOICE = [("doctor", "Врач"), ("dispatcher", "Диспетчер")]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    surname = models.CharField(max_length=256, blank=False, verbose_name="Отчество")
    role = models.CharField(max_length=20, choices=ROLE_CHOICE, default="doctor", verbose_name="Роль")
    uuid_session = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, verbose_name="Идентификатор сессии"
    )
    session_expire = models.DateTimeField(
        default= get_expire_time(), verbose_name="Срок действия сессии"
    )

    @property
    def uuid_is_active(self):
        return now() < self.session_expire

    def refresh_session(self, expire_days=30):
        self.uuid_session = uuid.uuid4()
        self.session_expire = now() + timedelta(days=expire_days)
        self.save(update_fields=["uuid_session", "session_expire"])

    def invalidate_all_session(self):
        self.refresh_session(expire_days=0)
    def __str__(self):
                return f"{self.user.username} ({self.get_role_display()})"
    class Meta:
        db_table = "profiles"

        indexes = [models.Index(fields=["uuid_session"]), models.Index(fields=["session_expire"])]

        


class RefreshToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='refresh_tokens')
    jti =  models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, verbose_name="Идентификатор токена"
    )
    created = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=get_token_expire_time,verbose_name="Срок жизни токена")
    revoked = models.BooleanField(default=False)

    @property
    def jti_is_active(self):
        return now() < self.expires_at

    def refresh(self, expire_days=7):
        self.jti = uuid.uuid4()
        self.expires_at = now() + timedelta(days=expire_days)
        self.save(update_fields=["expires_at", "jti"])

    def __str__(self):
                return f"{self.user.username} | {self.jti} | {'revoked' if self.revoked else 'active'}"
    class Meta:
        db_table = 'refresh'

        indexes = [models.Index(fields=["jti"]), models.Index(fields=["revoked"])]

        