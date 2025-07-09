# populate_db.py
import os
import django
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from django.contrib.auth.models import User
from user.models import Profile
from card.models import Card

def create_users():
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

def create_cards():
    cards = [
        Card(
            id=1,
            doctor_id=1,
            first_name="Петр",
            last_name="Сидоров",
            surname="Алексеевич",
            address="ул. Ленина, 1",
            date_of_birth=date(1980, 5, 20),
            crew=101,
            cause="Высокая температура",
            status="Выполнено",
            date_card="2024-06-01",
            time_of_receipt="10:00",
            transmission_time="10:05",
            departure_time="10:10",
            arrival_time="10:20",
            start_time_of_hospitalization="10:30",
            time_of_arrival_at_hospital="10:50",
            call_end_time="11:00",
            zhaloby="Жалуется на жар и слабость",
            anamnesis="Болел ОРВИ неделю назад",
            general_assessment="Средней тяжести",
            сonsciousness="Ясное",
            glasgow_scale=15,
            body_position="Лежа",
            temperature_before=39.0,
            respiratory_rate_before=20,
            heartbite_before=90,
            saturation_before=97,
            pulse_before=90,
            blood_pressure_systolic_before=120,
            blood_pressure_diastolic_before=80,
            normal_blood_pressure_systolic=120,
            normal_blood_pressure_diastolic=80,
            blood_glucose_before=5.2,
            dry_skin="Нет",
            color_skin="Розовая",
            jaundice="Нет",
            rash="Нет",
            throat="Горло красное",
            tonsils="Увеличены",
            lymph_nodes="Не увеличены",
            swelling="Нет",
            respiratory_type="Грудной",
            wheezing="Нет",
            wheezing_localisation="",
            dyspnea="Нет",
            heart_rate_deficit=False,
            heart_tone_accent="Нет",
            rhythmic_tone="Ритмичные",
            tone_of_heart="Нормальные",
            murmur="Нет",
            rhythmic_pulse="Ритмичный",
            characteristic_pulse="Нормальный",
            liver="Не увеличена",
            pain_stomach="Нет",
            characteristic_stomach="Мягкий",
            involved_in_the_act_of_breathing=False,
            formed_type_stool="Оформленный",
            regular_stool="Регулярный",
            rate_stool=1,
            is_shchetkin_blumberg=False,
            is_voskresensky=False,
            is_ortner=False,
            is_rovzinga=False,
            is_pasternatsky=False,
            is_sitkovsky=False,
            is_obraztsova=False,
            is_murphy=False,
            behaviour="Спокойное",
            reaction_to_light="Нормальная",
            pupils_of_the_eyes="Одинаковые",
            anisocoria=False,
            nystagmus=False,
            focal_signs=False,
            speech="Чёткая",
            none_symptoms=False,
            nuchal_rigidity=False,
            is_kernig_symptom=False,
            is_brudzinski_symptom=False,
            paralysis="Нет",
            sensitive="Сохранена",
            kidney_punch="Отрицательный",
            characteristic_urine="Светлая",
            painless_urination="Да",
            characteristic_urination="Нормальная",
            status_localis="Без особенностей",
            ecg_before="Синусовый ритм",
            ecg_after="Синусовый ритм",
            aid="Жаропонижающее",
            temperature_after=37.2,
            respiratory_rate_after=18,
            heartbite_after=80,
            saturation_after=98,
            pulse_after=80,
            blood_pressure_systolic_after=120,
            blood_pressure_diastolic_after=80,
            blood_glucose_after=5.1,
            diagnosis="ОРВИ",
            mkb="J06.9"
        ),
        # Можно добавить ещё карточки по аналогии
    ]
    for card in cards:
        Card.objects.update_or_create(id=card.id, defaults=card.__dict__)

if __name__ == "__main__":
    create_users()
    create_cards()
    print("База успешно наполнена тестовыми пользователями и карточками.")