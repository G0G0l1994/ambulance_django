#!/usr/bin/env python
"""
Скрипт для создания тестовых карт скорой помощи
Использование: python create_test_cards.py
"""

import os
import django
from datetime import date, datetime, time
from decimal import Decimal

# Настройка Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from django.contrib.auth.models import User
from django.utils import timezone
from user.models import Profile
from card.models import (
    Patient, Card, DateTimeData, CommonData, ParametersBefore, 
    SkinData, AirData, HeartData, StomachData, NervousData,
    UrinaryData, ECGData, AIDData, ParametersAfter, DiagnosisData
)


def create_test_cards():
    """Создание тестовых карт с указанными ID пользователей"""
    
    # Получаем пользователя и профиль
    try:
        user = User.objects.get(id=32)
        profile = Profile.objects.get(id=15)
        print(f"Найден пользователь: {user.username} (ID: {user.id})")
        print(f"Найден профиль: {profile} (ID: {profile.id})")
    except User.DoesNotExist:
        print("Ошибка: Пользователь с ID 32 не найден")
        return
    except Profile.DoesNotExist:
        print("Ошибка: Профиль с ID 15 не найден")
        return

    # Создаем тестовых пациентов
    patients_data = [
        {
            'first_name': 'Александр',
            'last_name': 'Петров',
            'surname': 'Иванович',
            'address': 'ул. Ленина, 15, кв. 23',
            'date_of_birth': date(1985, 3, 12)
        },
        {
            'first_name': 'Мария',
            'last_name': 'Сидорова',
            'surname': 'Петровна',
            'address': 'пр. Мира, 45, кв. 7',
            'date_of_birth': date(1978, 7, 25)
        },
        {
            'first_name': 'Дмитрий',
            'last_name': 'Козлов',
            'surname': 'Александрович',
            'address': 'ул. Гагарина, 8, кв. 12',
            'date_of_birth': date(1992, 11, 8)
        },
        {
            'first_name': 'Елена',
            'last_name': 'Морозова',
            'surname': 'Дмитриевна',
            'address': 'ул. Пушкина, 33, кв. 5',
            'date_of_birth': date(1980, 9, 15)
        },
        {
            'first_name': 'Сергей',
            'last_name': 'Волков',
            'surname': 'Сергеевич',
            'address': 'пр. Победы, 67, кв. 18',
            'date_of_birth': date(1975, 4, 30)
        }
    ]

    # Создаем пациентов
    patients = []
    for i, patient_data in enumerate(patients_data, 1):
        patient, created = Patient.objects.get_or_create(
            first_name=patient_data['first_name'],
            last_name=patient_data['last_name'],
            surname=patient_data['surname'],
            defaults=patient_data
        )
        patients.append(patient)
        print(f"Пациент {i}: {patient.get_full_name()}")

    # Данные для карт
    cards_data = [
        {
            'id': 1001,
            'crew': 101,
            'cause': 'Высокая температура, кашель',
            'status': 'completed',
            'datetime_data': {
                'time_of_receipt': timezone.make_aware(datetime(2024, 1, 15, 14, 30)),
                'transmission_time': timezone.make_aware(datetime(2024, 1, 15, 14, 35)),
                'departure_time': timezone.make_aware(datetime(2024, 1, 15, 14, 40)),
                'arrival_time': timezone.make_aware(datetime(2024, 1, 15, 14, 55)),
                'call_end_time': timezone.make_aware(datetime(2024, 1, 15, 15, 30))
            },
            'common_data': {
                'complaints': 'Жалуется на высокую температуру 39°C, сухой кашель, слабость',
                'anamnesis': 'Заболел 3 дня назад, лечился самостоятельно',
                'general_assessment': 'moderate',
                'сonsciousness': 'clear',
                'glasgow_scale': 15,
                'body_position': 'active',
                'status_localis': 'Без особенностей'
            },
            'parameters_before': {
                'temperature_before': 39.2,
                'respiratory_rate_before': 22,
                'heartbite_before': 95,
                'saturation_before': 96,
                'pulse_before': 95,
                'blood_pressure_systolic_before': 130,
                'blood_pressure_diastolic_before': 85,
                'blood_glucose_before': 5.8
            },
            'skin_data': {
                'dry_skin': 'dry',
                'color_skin': 'hyperemic',
                'jaundice': 'Нет',
                'rash': 'none',
                'throat': 'hyperemic',
                'tonsils': 'Не увеличены',
                'lymph_nodes': 'Не увеличены',
                'swelling': 'none'
            },
            'air_data': {
                'respiratory_type': 'vesicular',
                'wheezing': 'dry',
                'wheezing_localisation': 'Бронхи',
                'dyspnea': 'none'
            },
            'heart_data': {
                'heart_rate_deficit': False,
                'heart_tone_accent': 'Нет',
                'rhythmic_tone': 'rhythmic',
                'tone_of_heart': 'clear',
                'murmur': 'none',
                'rhythmic_pulse': 'rhythmic',
                'characteristic_pulse': 'normal'
            },
            'stomach_data': {
                'liver': 'Не увеличена',
                'pain_stomach': 'Нет',
                'characteristic_stomach': 'painless',
                'involved_in_the_act_of_breathing': True,
                'formed_type_stool': 'formed',
                'regular_stool': 'regular',
                'rate_stool': 1
            },
            'nervous_data': {
                'behaviour': 'calm',
                'reaction_to_light': 'yes',
                'pupils_of_the_eyes': 'normal',
                'anisocoria': False,
                'nystagmus': False,
                'focal_signs': False,
                'speech': 'clear',
                'none_symptoms': True,
                'nuchal_rigidity': False,
                'paralysis': 'none',
                'sensitive': 'preserved'
            },
            'urinary_data': {
                'kidney_punch': 'negative_both',
                'characteristic_urine': 'light_yellow',
                'with_inclusions': False,
                'with_sediment': False,
                'painless_urination': 'painless',
                'characteristic_urination': 'free'
            },
            'ecg_data': {
                'ecg_before': 'Синусовый ритм, ЧСС 95 уд/мин',
                'ecg_after': 'Синусовый ритм, ЧСС 85 уд/мин'
            },
            'aid_data': {
                'aid': 'Жаропонижающие препараты, обильное питье',
                'aid_effect': 'improvement'
            },
            'parameters_after': {
                'temperature_after': 37.8,
                'respiratory_rate_after': 18,
                'heartbite_after': 85,
                'saturation_after': 98,
                'pulse_after': 85,
                'blood_pressure_systolic_after': 125,
                'blood_pressure_diastolic_after': 80,
                'blood_glucose_after': 5.5
            },
            'diagnosis_data': {
                'diagnosis': 'ОРВИ',
                'mkb': 'J06.9'
            }
        },
        {
            'id': 1002,
            'crew': 102,
            'cause': 'Боль в груди',
            'status': 'completed',
            'datetime_data': {
                'time_of_receipt': timezone.make_aware(datetime(2024, 1, 16, 9, 15)),
                'transmission_time': timezone.make_aware(datetime(2024, 1, 16, 9, 20)),
                'departure_time': timezone.make_aware(datetime(2024, 1, 16, 9, 25)),
                'arrival_time': timezone.make_aware(datetime(2024, 1, 16, 9, 40)),
                'start_time_of_hospitalization': timezone.make_aware(datetime(2024, 1, 16, 10, 0)),
                'time_of_arrival_at_hospital': timezone.make_aware(datetime(2024, 1, 16, 10, 30)),
                'call_end_time': timezone.make_aware(datetime(2024, 1, 16, 10, 45))
            },
            'common_data': {
                'complaints': 'Острая боль за грудиной, отдающая в левую руку',
                'anamnesis': 'Боль возникла внезапно 30 минут назад',
                'general_assessment': 'severe',
                'сonsciousness': 'clear',
                'glasgow_scale': 15,
                'body_position': 'forced',
                'status_localis': 'Без особенностей'
            },
            'parameters_before': {
                'temperature_before': 36.8,
                'respiratory_rate_before': 24,
                'heartbite_before': 110,
                'saturation_before': 92,
                'pulse_before': 110,
                'blood_pressure_systolic_before': 160,
                'blood_pressure_diastolic_before': 95,
                'blood_glucose_before': 6.2
            },
            'skin_data': {
                'dry_skin': 'moist',
                'color_skin': 'pale',
                'jaundice': 'Нет',
                'rash': 'none',
                'throat': 'calm',
                'tonsils': 'Не увеличены',
                'lymph_nodes': 'Не увеличены',
                'swelling': 'none'
            },
            'air_data': {
                'respiratory_type': 'vesicular',
                'wheezing': 'none',
                'wheezing_localisation': '',
                'dyspnea': 'inspiratory'
            },
            'heart_data': {
                'heart_rate_deficit': False,
                'heart_tone_accent': 'Нет',
                'rhythmic_tone': 'rhythmic',
                'tone_of_heart': 'muffled',
                'murmur': 'none',
                'rhythmic_pulse': 'rhythmic',
                'characteristic_pulse': 'weak_filling'
            },
            'stomach_data': {
                'liver': 'Не увеличена',
                'pain_stomach': 'Нет',
                'characteristic_stomach': 'painless',
                'involved_in_the_act_of_breathing': True,
                'formed_type_stool': 'formed',
                'regular_stool': 'regular',
                'rate_stool': 1
            },
            'nervous_data': {
                'behaviour': 'excited',
                'reaction_to_light': 'yes',
                'pupils_of_the_eyes': 'normal',
                'anisocoria': False,
                'nystagmus': False,
                'focal_signs': False,
                'speech': 'clear',
                'none_symptoms': True,
                'nuchal_rigidity': False,
                'paralysis': 'none',
                'sensitive': 'preserved'
            },
            'urinary_data': {
                'kidney_punch': 'negative_both',
                'characteristic_urine': 'light_yellow',
                'with_inclusions': False,
                'with_sediment': False,
                'painless_urination': 'painless',
                'characteristic_urination': 'free'
            },
            'ecg_data': {
                'ecg_before': 'Синусовая тахикардия, ЧСС 110 уд/мин',
                'ecg_after': 'Синусовый ритм, ЧСС 90 уд/мин'
            },
            'aid_data': {
                'aid': 'Нитроглицерин, аспирин, кислород',
                'aid_effect': 'improvement'
            },
            'parameters_after': {
                'temperature_after': 36.8,
                'respiratory_rate_after': 18,
                'heartbite_after': 90,
                'saturation_after': 96,
                'pulse_after': 90,
                'blood_pressure_systolic_after': 140,
                'blood_pressure_diastolic_after': 85,
                'blood_glucose_after': 6.0
            },
            'diagnosis_data': {
                'diagnosis': 'Острый коронарный синдром',
                'mkb': 'I20.9'
            }
        },
        {
            'id': 1003,
            'crew': 103,
            'cause': 'Травма головы',
            'status': 'completed',
            'datetime_data': {
                'time_of_receipt': timezone.make_aware(datetime(2024, 1, 17, 16, 45)),
                'transmission_time': timezone.make_aware(datetime(2024, 1, 17, 16, 50)),
                'departure_time': timezone.make_aware(datetime(2024, 1, 17, 16, 55)),
                'arrival_time': timezone.make_aware(datetime(2024, 1, 17, 17, 10)),
                'call_end_time': timezone.make_aware(datetime(2024, 1, 17, 17, 45))
            },
            'common_data': {
                'complaints': 'Головная боль, тошнота после падения',
                'anamnesis': 'Упал с лестницы 2 часа назад',
                'general_assessment': 'moderate',
                'сonsciousness': 'confused',
                'glasgow_scale': 13,
                'body_position': 'passive',
                'status_localis': 'Ссадина на лбу'
            },
            'parameters_before': {
                'temperature_before': 37.1,
                'respiratory_rate_before': 18,
                'heartbite_before': 85,
                'saturation_before': 98,
                'pulse_before': 85,
                'blood_pressure_systolic_before': 140,
                'blood_pressure_diastolic_before': 90,
                'blood_glucose_before': 5.5
            },
            'skin_data': {
                'dry_skin': 'moist',
                'color_skin': 'normal',
                'jaundice': 'Нет',
                'rash': 'none',
                'throat': 'calm',
                'tonsils': 'Не увеличены',
                'lymph_nodes': 'Не увеличены',
                'swelling': 'face'
            },
            'air_data': {
                'respiratory_type': 'vesicular',
                'wheezing': 'none',
                'wheezing_localisation': '',
                'dyspnea': 'none'
            },
            'heart_data': {
                'heart_rate_deficit': False,
                'heart_tone_accent': 'Нет',
                'rhythmic_tone': 'rhythmic',
                'tone_of_heart': 'clear',
                'murmur': 'none',
                'rhythmic_pulse': 'rhythmic',
                'characteristic_pulse': 'normal'
            },
            'stomach_data': {
                'liver': 'Не увеличена',
                'pain_stomach': 'Нет',
                'characteristic_stomach': 'painless',
                'involved_in_the_act_of_breathing': True,
                'formed_type_stool': 'formed',
                'regular_stool': 'regular',
                'rate_stool': 1
            },
            'nervous_data': {
                'behaviour': 'calm',
                'reaction_to_light': 'yes',
                'pupils_of_the_eyes': 'normal',
                'anisocoria': False,
                'nystagmus': True,
                'focal_signs': False,
                'speech': 'clear',
                'none_symptoms': False,
                'nuchal_rigidity': False,
                'paralysis': 'none',
                'sensitive': 'preserved'
            },
            'urinary_data': {
                'kidney_punch': 'negative_both',
                'characteristic_urine': 'light_yellow',
                'with_inclusions': False,
                'with_sediment': False,
                'painless_urination': 'painless',
                'characteristic_urination': 'free'
            },
            'ecg_data': {
                'ecg_before': 'Синусовый ритм, ЧСС 85 уд/мин',
                'ecg_after': 'Синусовый ритм, ЧСС 80 уд/мин'
            },
            'aid_data': {
                'aid': 'Обезболивающие, холод на место травмы',
                'aid_effect': 'improvement'
            },
            'parameters_after': {
                'temperature_after': 37.0,
                'respiratory_rate_after': 16,
                'heartbite_after': 80,
                'saturation_after': 98,
                'pulse_after': 80,
                'blood_pressure_systolic_after': 135,
                'blood_pressure_diastolic_after': 85,
                'blood_glucose_after': 5.3
            },
            'diagnosis_data': {
                'diagnosis': 'Сотрясение головного мозга',
                'mkb': 'S06.0'
            }
        }
    ]

    # Создаем карты
    for i, card_data in enumerate(cards_data):
        # Создаем основную карту
        card, created = Card.objects.get_or_create(
            id=card_data['id'],
            defaults={
                'doctor_id': user,
                'patient_id': patients[i % len(patients)],
                'crew': card_data['crew'],
                'cause': card_data['cause'],
                'status': card_data['status']
            }
        )
        
        if created:
            print(f"Создана карта {card.id}: {card.cause}")
            
            # Создаем связанные данные
            DateTimeData.objects.get_or_create(
                card_id=card,
                defaults=card_data['datetime_data']
            )
            
            CommonData.objects.get_or_create(
                card_id=card,
                defaults=card_data['common_data']
            )
            
            ParametersBefore.objects.get_or_create(
                card_id=card,
                defaults=card_data['parameters_before']
            )
            
            SkinData.objects.get_or_create(
                card_id=card,
                defaults=card_data['skin_data']
            )
            
            AirData.objects.get_or_create(
                card_id=card,
                defaults=card_data['air_data']
            )
            
            HeartData.objects.get_or_create(
                card_id=card,
                defaults=card_data['heart_data']
            )
            
            StomachData.objects.get_or_create(
                card_id=card,
                defaults=card_data['stomach_data']
            )
            
            NervousData.objects.get_or_create(
                card_id=card,
                defaults=card_data['nervous_data']
            )
            
            UrinaryData.objects.get_or_create(
                card_id=card,
                defaults=card_data['urinary_data']
            )
            
            ECGData.objects.get_or_create(
                card_id=card,
                defaults=card_data['ecg_data']
            )
            
            AIDData.objects.get_or_create(
                card_id=card,
                defaults=card_data['aid_data']
            )
            
            ParametersAfter.objects.get_or_create(
                card_id=card,
                defaults=card_data['parameters_after']
            )
            
            DiagnosisData.objects.get_or_create(
                card_id=card,
                defaults=card_data['diagnosis_data']
            )
        else:
            print(f"Карта {card.id} уже существует")

    print(f"\n✅ Создано {len(cards_data)} тестовых карт")
    print(f"👨‍⚕️ Врач: {user.get_full_name()} (ID: {user.id})")
    print(f"📋 Профиль: {profile} (ID: {profile.id})")


if __name__ == "__main__":
    print("🚑 Создание тестовых карт скорой помощи...")
    create_test_cards()
    print("✅ Готово!") 