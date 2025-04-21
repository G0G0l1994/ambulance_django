import time

from django.test import TestCase
from django.contrib.auth.models import User


class ProfileSessionsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='test')
        self.profile = self.user.profile

    def test_session_refresh(self):

        old_uuid = self.profile.uuid_session
        self.profile.refresh_session()
        self.assertNotEqual(old_uuid,self.profile.uuid_session)
        self.assertTrue(self.profile.uuid_is_active)
    
    def test_session_invalidation(self):
        self.profile.invalidate_all_session()
        self.assertFalse(self.profile.uuid_is_active)
