import logging
import uuid

from django.db import models, IntegrityError
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now, timedelta

logger = logging.getLogger(__name__)

class Profile(models.Model):

    ROLE_CHOICE = [
        ('doctor', 'Врач'),
        ('dispatcher', 'Диспетчер')
    ]

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    surname = models.CharField(
        max_length=256,
        blank=True,
        verbose_name="Отчество")
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICE,
        default='doctor',
        verbose_name="Роль"
    )
    uuid_session = models.UUIDField(default=uuid.uuid4, 
                                     editable=False,
                                     unique=True,
                                     verbose_name='Идентификатор сессии'
                                     )
    session_expire = models.DateTimeField(default= now, 
                                          verbose_name='Срок действия сессии'
                                          )

    @property
    def uuid_is_active(self):
        return now() < self.session_expire
    

    def refresh_session(self,expire_days=30):
        
        self.uuid_session = uuid.uuid4()
        self.session_expire = now() + timedelta(days=expire_days)
        self.save(update_fields=['uuid_session','session_expire'])
    
    def invalidate_all_session(self):
        self.refresh_session(expire_days=0)

    class Meta:
        db_table = 'profiles'

        indexes = [
        models.Index(fields=['uuid_session']),
        models.Index(fields=['session_expire'])
    ]
        
        def __str__(self):
            return f"{self.user.username} ({self.get_role_display()})"

@receiver(post_save,sender=User)      
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
            logger.info(f'{instance.username} created!')
        except IntegrityError as e:
            logger.error(f"Profile creation failed for user {instance.pk} error: {str(e)}")

@receiver(post_save,sender=User)
def save_user(sender,instance,**kwargs):
    instance.profile.save()