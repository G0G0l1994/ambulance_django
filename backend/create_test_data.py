#!/usr/bin/env python
"""
Скрипт для создания тестовых карт скорой помощи
Использование: python create_test_cards.py
"""
import os
import django
from datetime import date, datetime, timedelta
from faker import Faker
from random import randint
# Настройка Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from django.contrib.auth.models import User
from django.utils import timezone
from user.models import Profile, Crew
from card.models import (
    Patient, Card, DateTimeData, CommonData, ParametersBefore, 
    SkinData, AirData, HeartData, StomachData, NervousData,
    UrinaryData, ECGData, AIDData, ParametersAfter, DiagnosisData
)
from card.constants import *


def random_patient_list():
    fake = Faker(["ru_RU"])
    patient_data = []
    for _ in range(10):
        patient_data.append({
        'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'surname': fake.middle_name_male()[:-2]+"на",
            
            'date_of_birth': fake.date_of_birth(minimum_age=1, maximum_age=100)

    })
    return patient_data

def random_card_data():
    fake = Faker(["ru_RU"])
    
    fake_data = fake.date_time()
    diagnosis_choice = DIAGNOSIS_TEST[randint(0,len(DIAGNOSIS_TEST)-1)]
    card = {
        'crew': randint(101,103),
            'cause': CAUSES_TEST[randint(0,len(CAUSES_TEST)-1)],
            'status': CARD_STATUS_CHOICES[randint(0,len(CARD_STATUS_CHOICES)-1)][0],
            'address': fake.street_address(),
            'datetime_data': {
                'time_of_receipt': timezone.make_aware(fake_data + timedelta(minutes=10)),
                'transmission_time': timezone.make_aware(fake_data + timedelta(minutes=12)),
                'departure_time': timezone.make_aware(fake_data + timedelta(minutes=13)),
                'arrival_time': timezone.make_aware(fake_data + timedelta(minutes=23)),
                'call_end_time': timezone.make_aware(fake_data + timedelta(minutes=40))
            },
            'common_data': {
                'complaints': COMPLAINTS_TEST[randint(0,len(COMPLAINTS_TEST)-1)],
                'anamnesis': ANAMNESIS_TEST[randint(0,len(ANAMNESIS_TEST)-1)],
                'general_assessment': GENERAL_ASSESSMENT_CHOICES[randint(0,len(GENERAL_ASSESSMENT_CHOICES)-1)][0],
                'consciousness': CONSCIOUSNESS_CHOICES[randint(0,len(CONSCIOUSNESS_CHOICES)-1)][0],
                'glasgow_scale': randint(VALIDATION_LIMITS['glasgow_scale']['min'],VALIDATION_LIMITS['glasgow_scale']['max']),
                'body_position': BODY_POSITION_CHOICES[randint(0,len(BODY_POSITION_CHOICES)-1)][0],
                'status_localis': LOCAL_STATUS_TEST[randint(0,len(LOCAL_STATUS_TEST)-1)]
            },
            'parameters_before': {
                'temperature_before': float(f'{randint(int(VALIDATION_LIMITS['temperature']['min']),int(VALIDATION_LIMITS['temperature']['max'])) + float(randint(1,10)/10)}'),
                'respiratory_rate_before': randint(VALIDATION_LIMITS['respiratory_rate']['min'],VALIDATION_LIMITS['respiratory_rate']['max']),
                'heartbite_before': randint(VALIDATION_LIMITS['heart_rate']['min'],VALIDATION_LIMITS['heart_rate']['max']),
                'saturation_before': randint(VALIDATION_LIMITS['saturation']['min'],VALIDATION_LIMITS['saturation']['max']),
                'pulse_before': randint(VALIDATION_LIMITS['heart_rate']['min'],VALIDATION_LIMITS['heart_rate']['max']),
                'blood_pressure_systolic_before': randint(VALIDATION_LIMITS['blood_pressure_systolic']['min'],VALIDATION_LIMITS['blood_pressure_systolic']['max']),
                'blood_pressure_diastolic_before': randint(VALIDATION_LIMITS['blood_pressure_diastolic']['min'],VALIDATION_LIMITS['blood_pressure_diastolic']['max']),
                'blood_glucose_before': float(f'{randint(int(VALIDATION_LIMITS['blood_glucose']['min']),int(VALIDATION_LIMITS['blood_glucose']['max'])) + float(randint(1,10)/10)}')
            },
            'skin_data': {
                'dry_skin': SKIN_DRYNESS_CHOICES[randint(0,len(SKIN_DRYNESS_CHOICES)-1)][0],
                'color_skin': SKIN_COLOR_CHOICES[randint(0,len(SKIN_COLOR_CHOICES)-1)][0],
                'jaundice': 'Нет',
                'rash': RASH_CHOICES[randint(0,len(RASH_CHOICES)-1)][0],
                'throat': THROAT_CHOICES[randint(0,len(THROAT_CHOICES)-1)][0],
                'tonsils': 'Не увеличены',
                'lymph_nodes': 'Не увеличены',
                'swelling': SWELLING_CHOICES[randint(0,len(SWELLING_CHOICES)-1)][0]
            },
            'air_data': {
                'respiratory_type':RESPIRATORY_TYPE_CHOICES[randint(0,len(RESPIRATORY_TYPE_CHOICES)-1)][0],
                'wheezing': WHEEZING_CHOICES[randint(0,len(WHEEZING_CHOICES)-1)][0],
                'wheezing_localisation': 'Бронхи',
                'dyspnea': DYSPNEA_CHOICES[randint(0,len(DYSPNEA_CHOICES)-1)][0]
            },
            'heart_data': {
                'heart_rate_deficit': BOOLEAN_CHOICES_TEST[randint(0,1)],
                'heart_tone_accent': 'Нет',
                'rhythmic_tone': RHYTHMIC_CHOICES[randint(0,len(RHYTHMIC_CHOICES)-1)][0],
                'tone_of_heart': TONE_OF_HEART_CHOICES[randint(0,len(TONE_OF_HEART_CHOICES)-1)][0],
                'murmur': MURMUR_CHOICES[randint(0,len(MURMUR_CHOICES)-1)][0],
                'rhythmic_pulse': RHYTHMIC_CHOICES[randint(0,len(RHYTHMIC_CHOICES)-1)][0],
                'characteristic_pulse': CHARACTERISTIC_PULSE_CHOICES[randint(0,len(CHARACTERISTIC_PULSE_CHOICES)-1)][0]
            },
            'stomach_data': {
                'liver': 'Не увеличена',
                'pain_stomach': PAIN_STOMACH_CHOICES[randint(0,len(PAIN_STOMACH_CHOICES)-1)][0],
                'characteristic_stomach': CHARACTERISTIC_STOMACH_CHOICES[randint(0,len(CHARACTERISTIC_STOMACH_CHOICES)-1)][0],
                'involved_in_the_act_of_breathing': BOOLEAN_CHOICES_TEST[randint(0,1)],
                'formed_type_stool': FORMED_TYPE_STOOL_CHOICES[randint(0,len(FORMED_TYPE_STOOL_CHOICES)-1)][0],
                'regular_stool': REGULAR_STOOL_CHOICES[randint(0,len(REGULAR_STOOL_CHOICES)-1)][0],
                'rate_stool': randint(int(VALIDATION_LIMITS['rate_stool']['min']),int(VALIDATION_LIMITS['rate_stool']['max']))
            },
            'nervous_data': {
                'behaviour': BEHAVIOUR_CHOICES[randint(0,len(BEHAVIOUR_CHOICES)-1)][0],
                'reaction_to_light': REACTION_TO_LIGHT[randint(0,len(REACTION_TO_LIGHT)-1)][0],
                'pupils_of_the_eyes': PUPILS_OF_THE_EYES_CHOICES[randint(0,len(PUPILS_OF_THE_EYES_CHOICES)-1)][0],
                'anisocoria': BOOLEAN_CHOICES_TEST[randint(0,1)],
                'nystagmus': BOOLEAN_CHOICES_TEST[randint(0,1)],
                'focal_signs': BOOLEAN_CHOICES_TEST[randint(0,1)],
                'speech': SPEECH_CHOICES[randint(0,len(SPEECH_CHOICES)-1)][0],
                'none_symptoms': BOOLEAN_CHOICES_TEST[randint(0,1)],
                'nuchal_rigidity': BOOLEAN_CHOICES_TEST[randint(0,1)],
                'paralysis': PARALYSIS_CHOICES[randint(0,len(PARALYSIS_CHOICES)-1)][0],
                'sensitive': SENSITIVE_CHOICES[randint(0,len(SENSITIVE_CHOICES)-1)][0]
            },
            'urinary_data': {
                'kidney_punch': KIDNEY_PUNCH_CHOICES[randint(0,len(KIDNEY_PUNCH_CHOICES)-1)][0],
                'characteristic_urine': CHARACTERISTIC_URINE_CHOICES[randint(0,len(CHARACTERISTIC_URINE_CHOICES)-1)][0],
                'with_inclusions': BOOLEAN_CHOICES_TEST[randint(0,1)],
                'with_sediment': BOOLEAN_CHOICES_TEST[randint(0,1)],
                'painless_urination': PAINLESS_URINATION_CHOICES[randint(0,len(PAINLESS_URINATION_CHOICES)-1)][0],
                'characteristic_urination': CHARACTERISTIC_URINATION_CHOICES[randint(0,len(CHARACTERISTIC_URINATION_CHOICES)-1)][0]
            },
            'ecg_data': {
                'ecg_before': f'Синусовый ритм, ЧСС f{randint(60, 120)} уд/мин',
                'ecg_after': f'Синусовый ритм, ЧСС {randint(60,120)} уд/мин'
            },
            'aid_data': {
                'aid': AID[randint(0,len(AID)-1)],
                'aid_effect': AID_EFFECTS[randint(0,len(AID_EFFECTS)-1)][0]
            },
            'parameters_after': {
                'temperature_before': float(f'{randint(int(VALIDATION_LIMITS['temperature']['min']),int(VALIDATION_LIMITS['temperature']['max'])) + float(randint(1,10)/10)}'),
                'respiratory_rate_before': randint(VALIDATION_LIMITS['respiratory_rate']['min'],VALIDATION_LIMITS['respiratory_rate']['max']),
                'heartbite_before': randint(VALIDATION_LIMITS['heart_rate']['min'],VALIDATION_LIMITS['heart_rate']['max']),
                'saturation_before': randint(VALIDATION_LIMITS['saturation']['min'],VALIDATION_LIMITS['saturation']['max']),
                'pulse_before': randint(VALIDATION_LIMITS['heart_rate']['min'],VALIDATION_LIMITS['heart_rate']['max']),
                'blood_pressure_systolic_before': randint(VALIDATION_LIMITS['blood_pressure_systolic']['min'],VALIDATION_LIMITS['blood_pressure_systolic']['max']),
                'blood_pressure_diastolic_before': randint(VALIDATION_LIMITS['blood_pressure_diastolic']['min'],VALIDATION_LIMITS['blood_pressure_diastolic']['max']),
                'blood_glucose_before': float(f'{randint(int(VALIDATION_LIMITS['blood_glucose']['min']),int(VALIDATION_LIMITS['blood_glucose']['max'])) + float(randint(1,10)/10)}')
            },
            'diagnosis_data': {
                'diagnosis': diagnosis_choice[0],
                'mkb': diagnosis_choice[1]
            }
    }
    print(card)
    return card

def create_test_cards():
    """Создание тестовых карт с указанными ID пользователей"""
    fake = Faker(["ru_RU"])
    # Получаем пользователя и профиль
    users = [
        {"username": "doctor1", "password": "pass1234", "first_name": "Иван", "last_name": "Иванов", "role": "doctor", "surname": "Иванович"},
        {"username": "dispatcher1", "password": "pass1234", "first_name": "Анна", "last_name": "Петрова", "role": "dispatcher", "surname": "Сергеевна"},
    ]
    for u in users:
        user, created = User.objects.get_or_create(username=u["username"], defaults={
            "first_name": u["first_name"],
            "last_name": u["last_name"],
        })
        if created:
            user.set_password(u["password"])
            user.save()
        Profile.objects.get_or_create(user=user, defaults={
            "role": u["role"],
            "surname": u["surname"],
        })

    crews = [
        {'crew_number': 101},
        {'crew_number': 102}
    ]
    for c in crews:
        crew, created = Crew.objects.get_or_create(crew_number=c["crew_number"])
        if created:
            crew.save()


    # Создаем тестовых пациентов

    
    patients_data = random_patient_list()
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

    
    cards_data = [random_card_data() for _ in range(len(patients))]
    # Создаем карты
    for i, card_data in enumerate(cards_data):
        # Создаем основную карту
        card = Card.objects.create(
            **{
                'doctor_id': user,
                'patient_id': patients[i % len(patients)],
                'crew': card_data['crew'],
                'cause': card_data['cause'],
                'status': card_data['status'],
                "address": card_data['address']
            }
        )
        print(f"Создана карта {card.id}: {card.cause}")
            # Создаем связанные данные
        DateTimeData.objects.get_or_create(
                card_id=card.id,
                defaults=card_data['datetime_data']
            )     
        CommonData.objects.get_or_create(
                card_id=card.id,
                defaults=card_data['common_data']
            )
        ParametersBefore.objects.get_or_create(
                card_id=card.id,
                defaults=card_data['parameters_before']
            )
        SkinData.objects.get_or_create(
                card_id=card.id,
                defaults=card_data['skin_data']
            )
        AirData.objects.get_or_create(
                card_id=card.id,
                defaults=card_data['air_data']
            )
        HeartData.objects.get_or_create(
                card_id=card.id,
                defaults=card_data['heart_data']
            )
        StomachData.objects.get_or_create(
                card_id=card.id,
                defaults=card_data['stomach_data']
            )
        NervousData.objects.get_or_create(
                card_id=card.id,
                defaults=card_data['nervous_data']
            )
        UrinaryData.objects.get_or_create(
                card_id=card.id,
                defaults=card_data['urinary_data']
            )
        ECGData.objects.get_or_create(
                card_id=card.id,
                defaults=card_data['ecg_data']
            )
        AIDData.objects.get_or_create(
                card_id=card.id,
                defaults=card_data['aid_data']
            )
        ParametersAfter.objects.get_or_create(
                card_id=card.id,
                defaults=card_data['parameters_after']
            )
        DiagnosisData.objects.get_or_create(
                card_id=card.id,
                defaults=card_data['diagnosis_data']
            )

    print(f"\n✅ Создано {len(cards_data)} тестовых карт")
    print(f"👨‍⚕️ Врач: {user.get_full_name()} (ID: {user.id})")
    print(f"📋 Профиль: {user.profile} (ID: {user.profile.id})")


if __name__ == "__main__":
    print("🚑 Создание тестовых карт скорой помощи...")
    create_test_cards()
    print("✅ Готово!") 