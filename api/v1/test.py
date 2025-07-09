from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from user.models import Profile, RefreshToken
from user.services.auth import create_refresh_token

class RefreshTokenObtainTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.profile = Profile.objects.create(user=self.user, surname='Test', role='doctor')
        self.refresh_token_obj = RefreshToken.objects.create(user=self.user)
        self.refresh_token = create_refresh_token(self.user)
        # Важно: jti в JWT и в базе должны совпадать!

    def test_refresh_token_success(self):
        url = reverse('refresh_token_obtain')  # или путь к твоему endpoint
        response = self.client.post(url, {'refresh': self.refresh_token}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)
        self.assertIsInstance(response.data['access'], str)

    def test_refresh_token_invalid(self):
        url = reverse('refresh_token_obtain')
        response = self.client.post(url, {'refresh': 'invalidtoken'}, format='json')
        self.assertEqual(response.status_code, 401)
        self.assertIn('detail', response.data)