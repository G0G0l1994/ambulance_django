from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from user.models import Profile, RefreshToken
from user.services.auth import create_refresh_token
from card.models import (
    Card, Patient, DateTimeData, CommonData, ParametersBefore, ParametersAfter,
    SkinData, AirData, HeartData, StomachData, NervousData, UrinaryData,
    ECGData, AIDData, DiagnosisData
)
from api.v1.serializers.card import CardUpdateSerializer, CardDetailSerializer, CardCreateSerializer
 
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

from django.test import TestCase
from django.contrib.auth.models import User
from card.models import (
    Card, Patient, DateTimeData, CommonData, ParametersBefore, ParametersAfter,
    SkinData, AirData, HeartData, StomachData, NervousData, UrinaryData,
    ECGData, AIDData, DiagnosisData
)
from api.v1.serializers.card import (
    CardCreateSerializer, CardUpdateSerializer, CardDetailSerializer
)
from datetime import date

class CardSerializersTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testdoc')
        self.patient = Patient.objects.create(
            first_name='Иван', last_name='Иванов', surname='Иванович',
            address='ул. Тестовая, 1', date_of_birth=date(1990, 1, 1)
        )
        self.card = Card.objects.create(
            id=1, doctor_id=self.user, patient_id=self.patient,
            crew=101, cause='Тестовая причина', status='created'
        )
        # Создаем связанные объекты для detail
        DateTimeData.objects.create(card_id=self.card)
        CommonData.objects.create(card_id=self.card)
        ParametersBefore.objects.create(card_id=self.card)
        ParametersAfter.objects.create(card_id=self.card)
        SkinData.objects.create(card_id=self.card)
        AirData.objects.create(card_id=self.card)
        HeartData.objects.create(card_id=self.card)
        StomachData.objects.create(card_id=self.card)
        NervousData.objects.create(card_id=self.card)
        UrinaryData.objects.create(card_id=self.card)
        ECGData.objects.create(card_id=self.card)
        AIDData.objects.create(card_id=self.card)
        DiagnosisData.objects.create(card_id=self.card)

    def test_card_create_serializer(self):
        data = {
            'doctor_id': self.user.id,
            'patient_id': self.patient.id,
            'crew': 102,
            'cause': 'Головная боль',
            'status': 'created',
            'common_data': {
                'complaints': 'Жалоба',
                'general_assessment': 'satisfactory',
                'сonsciousness': 'clear',
                'glasgow_scale': 15,
                'body_position': 'active'
            }
        }
        serializer = CardCreateSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        card = serializer.save()
        self.assertEqual(card.cause, 'Головная боль')
        self.assertEqual(card.doctor_id, self.user)
        self.assertEqual(card.patient_id, self.patient)
        self.assertTrue(CommonData.objects.filter(card_id=card).exists())

    def test_card_update_serializer(self):
        update_data = {
            'cause': 'Обновленная причина',
            'common_data': {
                'complaints': 'Обновленная жалоба',
                'general_assessment': 'moderate'
            }
        }
        serializer = CardUpdateSerializer(self.card, data=update_data, partial=True)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        card = serializer.save()
        self.assertEqual(card.cause, 'Обновленная причина')
        common = CommonData.objects.get(card_id=card)
        self.assertEqual(common.complaints, 'Обновленная жалоба')
        self.assertEqual(common.general_assessment, 'moderate')

    def test_card_detail_serializer(self):
        serializer = CardDetailSerializer(self.card)
        data = serializer.data
        self.assertEqual(data['id'], self.card.id)
        self.assertEqual(data['doctor']['id'], self.user.id)
        self.assertEqual(data['patient']['id'], self.patient.id)
        self.assertIn('common_data', data)
        self.assertIn('parameters_before_data', data)
        self.assertIn('skin_data', data)
        self.assertIn('diagnosis_data', data)