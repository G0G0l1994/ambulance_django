from datetime import date

from django.db import models
from django.contrib.auth.models import User


from .constants import *


class Patient(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100, null=True)
    
    date_of_birth = models.DateField(null=True)

    def get_full_name(self):
        return f"{self.last_name} {self.first_name} {self.surname}".strip()

    def get_full_age(self):

        if not self.date_of_birth:
            return None
        
        today = date.today()
        years = today.year - self.date_of_birth.year
        
        if today.month < self.date_of_birth.month or (
            today.month == self.date_of_birth.month and 
            today.day < self.date_of_birth.day
        ):
            years -= 1
            
        return years

    class Meta:
        db_table = "Patient"
    
    def __repr__(self):
        return f"{self.first_name} {self.surname} {self.last_name} {self.get_full_age}"

class Card(models.Model):
    doctor_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='doctor_cards')
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, related_name='patient_cards')
    crew = models.IntegerField(null=True)
    cause = models.CharField(max_length=256, null=True)
    status = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = "Card"

class DateTimeData(models.Model):
    card = models.ForeignKey(Card,on_delete=models.CASCADE, related_name='datetime_data')
    date_card = models.DateField(auto_now=True)  # дата карты
    time_of_receipt = models.DateTimeField(null=True)  # время приёма
    transmission_time = models.DateTimeField(null=True)  # время передачи
    departure_time = models.DateTimeField(null=True)  # время выезда бригады
    arrival_time = models.DateTimeField(null=True)  # время прибытия
    start_time_of_hospitalization = models.DateTimeField(null=True)  # время начала госпитализации
    time_of_arrival_at_hospital = models.DateTimeField(null=True)  # время прибытия в больницу
    call_end_time = models.DateTimeField(null=True)  # время окончания вызова

    class Meta:
        db_table = "DateTimeData"
    
class CommonData(models.Model):
    # общие сведения
    card = models.ForeignKey(Card,on_delete=models.CASCADE, related_name='common_data')
    complaints = models.TextField(null=True)
    anamnesis = models.TextField(null=True)
    general_assessment = models.CharField(max_length=100, null=True, choices=GENERAL_ASSESSMENT_CHOICES,default="satisfactory")
    сonsciousness = models.CharField(max_length=100, null=True, choices=CONSCIOUSNESS_CHOICES,default="clear")  # сознание
    glasgow_scale = models.IntegerField(null=True)  # шкала Глазго
    body_position = models.CharField(max_length=100, null=True, choices=BODY_POSITION_CHOICES, default='active')  # исправлено
    normal_blood_pressure_systolic = models.IntegerField(null=True,default=DEFAULT_VALUES['normal_blood_pressure_systolic'])
    normal_blood_pressure_diastolic = models.IntegerField(null=True, default=DEFAULT_VALUES['normal_blood_pressure_diastolic'])
    status_localis = models.TextField(null=True)
    
    class Meta:
        db_table = "CommonData"

class ParametersBefore(models.Model):
    # показатели до
    card = models.ForeignKey(Card,on_delete=models.CASCADE, related_name='parameters_before_data')
    temperature_before = models.FloatField(null=True)
    respiratory_rate_before = models.IntegerField(null=True)
    heartbite_before = models.IntegerField(null=True)
    saturation_before = models.IntegerField(null=True)
    pulse_before = models.IntegerField(null=True)
    blood_pressure_systolic_before = models.IntegerField(null=True)
    blood_pressure_diastolic_before = models.IntegerField(null=True)
    blood_glucose_before = models.FloatField(null=True)

    class Meta:
        db_table = "ParametersBefore"

class SkinData(models.Model):
    # кожные покровы
    card = models.ForeignKey(Card,on_delete=models.CASCADE, related_name='skin_data')
    dry_skin = models.CharField(max_length=100, null=True, choices=SKIN_DRYNESS_CHOICES,default="dry")
    color_skin = models.CharField(max_length=100, null=True, choices=SKIN_COLOR_CHOICES,default='normal')
    jaundice = models.CharField(max_length=100, null=True,default=DEFAULT_VALUES['jaundice'])  # желтушность
    rash = models.CharField(max_length=100, null=True, choices=RASH_CHOICES,default='none')  # сыпь
    throat = models.CharField(max_length=100, null=True, choices=THROAT_CHOICES,default='calm')  # зев
    tonsils = models.CharField(max_length=100, null=True,default=DEFAULT_VALUES['tonsils'])  # миндалины
    lymph_nodes = models.CharField(max_length=100, null=True,default=DEFAULT_VALUES['lymph_nodes'])  # лимфоузлы
    swelling = models.CharField(max_length=100, null=True,choices=SWELLING_CHOICES,default='none')  # отёки

    class Meta:
        db_table = "SkinData"

class AirData(models.Model):
    # дыхательная система
    card = models.ForeignKey(Card,on_delete=models.CASCADE, related_name='air_data')
    respiratory_type = models.CharField(max_length=100, null=True,choices=RESPIRATORY_TYPE_CHOICES,default='vesicular')
    wheezing = models.CharField(max_length=100, null=True,choices=WHEEZING_CHOICES,default='none')  # хрипы
    wheezing_localisation = models.CharField(max_length=100, null=True)  # локализация хрипов
    dyspnea = models.CharField(max_length=100, null=True,choices=DYSPNEA_CHOICES,default='none')  # одышка

    class Meta:
        db_table = "AirData"

class HeartData(models.Model):
    #сердечно-сосудистая система
    card = models.ForeignKey(Card,on_delete=models.CASCADE, related_name='heart_data')
    heart_rate_deficit = models.BooleanField(null=True,default=False)
    heart_tone_accent = models.CharField(max_length=100, null=True,default=DEFAULT_VALUES['heart_tone_accent'])  # акцент тона
    rhythmic_tone = models.CharField(max_length=100, null=True,choices=RHYTHMIC_TONE_CHOICES,default='rhythmic')
    tone_of_heart = models.CharField(max_length=100, null=True,choices=TONE_OF_HEART_CHOICES,default='clear')
    murmur = models.CharField(max_length=100, null=True,choices=MURMUR_CHOICES,default='none')
    rhythmic_pulse = models.CharField(max_length=100, null=True,choices=RHYTHMIC_PULSE_CHOICES,default='rhythmic')
    characteristic_pulse = models.CharField(max_length=100, null=True,choices=CHARACTERISTIC_PULSE_CHOICES,default='normal')

    class Meta:
        db_table = "HeartData"

class StomachData(models.Model):
    # живот
    card = models.ForeignKey(Card,on_delete=models.CASCADE, related_name='stomach_data')
    liver = models.CharField(max_length=100, null=True, default=DEFAULT_VALUES['liver'])  # печень
    pain_stomach = models.CharField(max_length=100, null=True)
    characteristic_stomach = models.CharField(max_length=100, null=True,choices=PAIN_STOMACH_CHOICES,default='painless')
    involved_in_the_act_of_breathing = models.BooleanField(null=True,default=True)
    formed_type_stool = models.CharField(max_length=100, null=True,choices=FORMED_TYPE_STOOL_CHOICES,default='formed')
    regular_stool = models.CharField(max_length=100, null=True,choices=REGULAR_STOOL_CHOICES,default='regular')
    rate_stool = models.IntegerField(null=True,default=DEFAULT_VALUES['rate_stool'])
    is_shchetkin_blumberg = models.BooleanField(null=True,default=False)
    is_voskresensky = models.BooleanField(null=True,default=False)
    is_ortner = models.BooleanField(null=True,default=False)
    is_rovzinga = models.BooleanField(null=True,default=False)
    is_pasternatsky = models.BooleanField(null=True,default=False)
    is_sitkovsky = models.BooleanField(null=True,default=False)
    is_obraztsova = models.BooleanField(null=True,default=False)
    is_murphy = models.BooleanField(null=True,default=False)

    class Meta:
        db_table = "StomachData"

class NervousData(models.Model):
    # нервная система
    card = models.ForeignKey(Card,on_delete=models.CASCADE, related_name='nervous_data')
    behaviour = models.CharField(max_length=100, null=True, choices=BEHAVIOUR_CHOICES,default='calm')
    reaction_to_light = models.CharField(max_length=100, null=True, choices=REACTION_TO_LIGHT,default='yes')
    pupils_of_the_eyes = models.CharField(max_length=100, null=True,choices=PUPILS_OF_THE_EYES_CHOICES,default='normal')
    anisocoria = models.BooleanField(null=True,default=False)
    nystagmus = models.BooleanField(null=True,default=False)
    focal_signs = models.BooleanField(null=True,default=False)
    speech = models.CharField(max_length=100, null=True,choices=SPEECH_CHOICES,default='clear')
    none_symptoms = models.BooleanField(null=True,default=True)
    nuchal_rigidity = models.BooleanField(null=True,default=False)
    is_kernig_symptom = models.BooleanField(null=True,default=False)
    is_brudzinski_symptom = models.BooleanField(null=True,default=False)
    paralysis = models.CharField(max_length=100, null=True,choices=PARALYSIS_CHOICES,default='none')
    sensitive = models.CharField(max_length=100, null=True,choices=SENSITIVE_CHOICES,default='preserved')

    class Meta:
        db_table = "NervousData"

class UrinaryData(models.Model):
    # мочеполовая система
    card = models.ForeignKey(Card,on_delete=models.CASCADE, related_name='urinary_data')
    kidney_punch = models.CharField(max_length=100, null=True,choices=KIDNEY_PUNCH_CHOICES,default='negative_both')  # симптом покалачивания
    characteristic_urine = models.CharField(max_length=100, null=True,choices=CHARACTERISTIC_URINE_CHOICES,default='light_yellow')
    with_inclusions = models.BooleanField(null=True,default=False)
    with_sediment = models.BooleanField(null=True,default=False)
    painless_urination = models.CharField(max_length=100, null=True,choices=PAINLESS_URINATION_CHOICES,default='painless')
    characteristic_urination = models.CharField(max_length=100, null=True,choices=CHARACTERISTIC_URINATION_CHOICES,default='free')

    class Meta:
        db_table = "UrinaryData"

class ECGData(models.Model):
    # ЭКГ
    card = models.ForeignKey(Card,on_delete=models.CASCADE, related_name='ecg_data')
    ecg_before = models.TextField(null=True)
    ecg_after = models.TextField(null=True)

    class Meta:
        db_table = "ECGData"

class AIDData(models.Model):
    # помощь
    card = models.ForeignKey(Card,on_delete=models.CASCADE, related_name='aid_data')
    aid = models.TextField(null=True)
    aid_effect = models.CharField(max_length=100, null=True, choices=AID_EFFECTS, default='improvement')

    class Meta:
        db_table = "AIDData"

class ParametersAfter(models.Model):
    # показатели после    
    card = models.ForeignKey(Card,on_delete=models.CASCADE, related_name='parameters_after_data')
    temperature_after = models.FloatField(null=True)
    respiratory_rate_after = models.IntegerField(null=True)
    heartbite_after = models.IntegerField(null=True)
    saturation_after = models.IntegerField(null=True)
    pulse_after = models.IntegerField(null=True)
    blood_pressure_systolic_after = models.IntegerField(null=True)
    blood_pressure_diastolic_after = models.IntegerField(null=True)
    blood_glucose_after = models.FloatField(null=True)

    class Meta:
        db_table = "ParametersAfter"

class DiagnosisData(models.Model):
    # диагноз
    card = models.ForeignKey(Card,on_delete=models.CASCADE, related_name='diagnosis_data')
    diagnosis = models.CharField(max_length=100, null=True)
    mkb = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = "DiagnosisData"
