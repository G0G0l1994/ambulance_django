from django.db import models


class Card(models.Model):
    id = models.IntegerField(primary_key = True)
    doctor_id = models.IntegerField(null=True)
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    surname = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    date_of_birth = models.DateField(null=True)
    crew = models.IntegerField(null=True)
    #повод к вызову
    cause = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)
    #время
    date_card = models.CharField(max_length=100,null=True) # дата карты
    time_of_receipt = models.CharField(max_length=100,null=True) # время приёма
    transmission_time = models.CharField(max_length=100,null=True) # время передачи
    departure_time = models.CharField(max_length=100,null=True) #время выезда бригады
    arrival_time = models.CharField(max_length=100,null=True) #время прибытия
    start_time_of_hospitalization = models.CharField(max_length=100,null=True) #время начала госпитализации
    time_of_arrival_at_hospital = models.CharField(max_length=100,null=True) #время прибытия в больницу
    call_end_time = models.CharField(max_length=100,null=True) # время окончания вызова
    #общие сведения
    zhaloby = models.TextField(null=True)
    anamnesis = models.TextField(null=True)
    general_assessment = models.CharField(max_length=100,null=True)
    сonsciousness = models.CharField(max_length=100,null=True) #сознание
    glasgow_scale = models.IntegerField(null=True) #шкала Глазго
    body_position = models.CharField(max_length=100,null=True) # положение тела
    #показатели до 
    temperature_before = models.FloatField(null=True)
    respiratory_rate_before = models.IntegerField(null=True)
    heartbite_before = models.IntegerField(null=True)
    saturation_before = models.IntegerField(null=True)
    pulse_before = models.IntegerField(null=True)
    blood_pressure_systolic_before = models.IntegerField(null=True)
    blood_pressure_diastolic_before = models.IntegerField(null=True)
    normal_blood_pressure_systolic = models.IntegerField(null=True) 
    normal_blood_pressure_diastolic = models.IntegerField(null=True)
    blood_glucose_before = models.FloatField(null=True)
    #кожные покровы
    dry_skin = models.CharField(max_length=100,null=True)
    color_skin = models.CharField(max_length=100,null=True)
    jaundice = models.CharField(max_length=100,null=True) #желтушность
    rash = models.CharField(max_length=100,null=True) #сыпь
    throat = models.CharField(max_length=100,null=True) #зев
    tonsils = models.CharField(max_length=100,null=True)#миндалины
    lymph_nodes = models.CharField(max_length=100,null=True) #лимфоузлы
    swelling = models.CharField(max_length=100,null=True) #отёки
    #дыхательная система
    respiratory_type = models.CharField(max_length=100,null=True)
    wheezing = models.CharField(max_length=100,null=True)# хрипы
    wheezing_localisation = models.CharField(max_length=100,null=True)# хрипы
    dyspnea = models.CharField(max_length=100,null=True) #одышка
    heart_rate_deficit = models.BooleanField(null=True)
    heart_tone_accent = models.CharField(max_length=100,null=True) #акцент тона
    rhythmic_tone = models.CharField(max_length=100,null=True)
    tone_of_heart=models.CharField(max_length=100,null=True)
    murmur = models.CharField(max_length=100,null=True)
    rhythmic_pulse = models.CharField(max_length=100,null=True)
    characteristic_pulse = models.CharField(max_length=100,null=True)
    #живот
    liver = models.CharField(max_length=100,null=True) # печень   
    pain_stomach = models.CharField(max_length=100,null=True)
    characteristic_stomach = models.CharField(max_length=100,null=True)
    involved_in_the_act_of_breathing = models.BooleanField(null=True)
    formed_type_stool = models.CharField(max_length=100,null=True)
    regular_stool = models.CharField(max_length=100,null=True)
    rate_stool = models.IntegerField(null=True)
    is_shchetkin_blumberg = models.BooleanField(null=True)
    is_voskresensky = models.BooleanField(null=True)
    is_ortner = models.BooleanField(null=True)
    is_rovzinga = models.BooleanField(null=True)
    is_pasternatsky = models.BooleanField(null=True)
    is_sitkovsky = models.BooleanField(null=True)
    is_obraztsova = models.BooleanField(null=True)
    is_murphy = models.BooleanField(null=True)
    #нервная система
    behaviour = models.CharField(max_length=100,null=True)
    reaction_to_light = models.CharField(max_length=100,null=True)
    pupils_of_the_eyes = models.CharField(max_length=100,null=True)
    anisocoria = models.BooleanField(null=True)
    nystagmus = models.BooleanField(null=True)
    focal_signs = models.BooleanField(null=True)
    speech = models.CharField(max_length=100,null=True)
    none_symptoms = models.BooleanField(null=True)
    nuchal_rigidity = models.BooleanField(null=True)
    is_kernig_symptom = models.BooleanField(null=True)
    is_brudzinski_symptom = models.BooleanField(null=True)
    paralysis = models.CharField(max_length=100,null=True)
    sensitive = models.CharField(max_length=100,null=True)
    #мочеполовая система
    kidney_punch = models.CharField(max_length=100,null=True) #симптом покалачивания
    characteristic_urine = models.CharField(max_length=100,null=True)
    painless_urination = models.CharField(max_length=100,null=True)
    characteristic_urination = models.CharField(max_length=100,null=True)
    #статус локалис
    status_localis = models.TextField(null=True)
    #ЭКГ
    ecg_before = models.TextField(null=True)
    ecg_after = models.TextField(null=True)
    #помощь
    aid = models.TextField(null=True)
    #показатели после
    temperature_after = models.FloatField(null=True)
    respiratory_rate_after = models.IntegerField(null=True)
    heartbite_after = models.IntegerField(null=True)
    saturation_after = models.IntegerField(null=True)
    pulse_after = models.IntegerField(null=True)
    blood_pressure_systolic_after = models.IntegerField(null=True)
    blood_pressure_diastolic_after = models.IntegerField(null=True)
    blood_glucose_after = models.FloatField(null=True)
    #диагноз
    diagnosis = models.CharField(max_length=100,null=True)
    mkb = models.CharField(max_length=100,null=True)
    submit = models.CharField(max_length=100,null=True)
    csrf_token = models.TextField(null=True)

    
        


    class Meta:
        db_table = "Card"
    
