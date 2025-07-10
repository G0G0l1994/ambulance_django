
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.conf import settings
from django.utils import timezone
from datetime import timedelta

import jwt

from .services.auth import create_jwt_token, validate_jwt_token
from .models import Profile


class ProfileSessionsTest(TestCase):

    def setUp(self):
        self.user: User = User.objects.create_user(username='test')
        self.profile = Profile.objects.create(user = self.user,surname='test_test',role='doctor')
        


    def test_session_refresh(self):

        old_uuid = self.profile.uuid_session
        self.profile.refresh_session()
        self.assertNotEqual(old_uuid,self.profile.uuid_session)
        self.assertTrue(self.profile.uuid_is_active)
    
    def test_session_invalidation(self):
        self.profile.invalidate_all_session()
        self.assertFalse(self.profile.uuid_is_active)

class AuthTest(TestCase):

    def setUp(self):
        self.user: User = User.objects.create_user(username='test_auth',
                                        password='test_user_1234',
                                        is_active=True)
        self.profile: Profile = Profile.objects.create(user = self.user,surname='test_test',role='doctor')

        self.factory = RequestFactory()
    def test_create_jwt(self):
        token = create_jwt_token(self.user)
        self.assertIsInstance(token, str)

        payload = jwt.decode(token,
                             key=settings.SECRET_KEY,
                             algorithms=['HS256'],
                             options={'verify_signature': False})
        self.assertEqual(payload['user_id'], str(self.user.id))

    def test_validation_token(self):
        token = create_jwt_token(self.user)
        user = validate_jwt_token(token)

        self.assertEqual(user, self.user)
    
    def test_expire_token(self):
        from django.utils import timezone

        payload = {
            "user_id": self.user.id,
            "uuid_session": str(self.profile.uuid_session),
            "exp": (timezone.now() - timedelta(hours=1)).timestamp()
        }


        token = jwt.encode(payload, 
                           key=settings.SECRET_KEY,
                           algorithm='HS256'
                           )
        self.assertIsNone(validate_jwt_token(token))

    def test_invalid_jwt_token(self):
        token = create_jwt_token(self.user)
        self.profile.refresh_session()

        self.assertIsNone(validate_jwt_token(token))
    
    def test_inactive_session(self):
        # Делаем сессию неактивной
        self.profile.session_expire = timezone.now() - timedelta(days=1)
        self.profile.save()
        self.assertFalse(self.profile.uuid_is_active)
        token = create_jwt_token(self.user)
        self.profile.refresh_session()
        self.assertTrue(self.profile.uuid_is_active)
        
    

