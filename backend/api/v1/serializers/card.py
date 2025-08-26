from email.policy import default
from django.utils import timezone
from rest_framework import serializers

from card.models import (
    Card,Patient,DateTimeData,ParametersBefore,ParametersAfter,CommonData,
    SkinData,AirData,HeartData,StomachData,NervousData,
    UrinaryData,ECGData,AIDData,DiagnosisData, MKB)
from api.v1.serializers.user import UserSerializer



class PatientSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name',read_only=True)
    full_age = serializers.IntegerField(source='get_full_age', read_only=True)

    class Meta:
        model = Patient
        fields = [
            'id','first_name','surname','last_name',
            'date_of_birth','full_name', 'full_age'
        ]

class DateTimeDataSerializer(serializers.ModelSerializer):
    
    time_of_receipt_label = serializers.CharField(default='Время приёма вызова')
    transmission_time_label = serializers.CharField(default="Время передачи вызова")
    departure_time_label = serializers.CharField(default='Время приёма бригадой')
    arrival_time_label = serializers.CharField(default='Время прибытия')
    start_time_of_hospitalization_label = serializers.CharField(default="Время госпитализации")
    time_of_arrival_at_hospital_label = serializers.CharField(default="Время прибытия в стационар")
    call_end_time_label = serializers.CharField(default="Время окончания вызова")

    class Meta:
        model = DateTimeData
        fields = [
            "id","date_card","time_of_receipt","transmission_time",
            "departure_time","arrival_time","start_time_of_hospitalization",
            "time_of_arrival_at_hospital","call_end_time",
            "time_of_receipt_label","transmission_time_label","departure_time_label",
            "arrival_time_label","start_time_of_hospitalization_label","time_of_arrival_at_hospital_label",
            "call_end_time_label"
        ]
    
    
    

class ParametersBeforeSerializer(serializers.ModelSerializer):
    
    


    class Meta:
        model = ParametersBefore
        fields  = [
            "id","temperature","respiratory_rate","heartbite",
            "saturation","pulse","blood_pressure_systolic",
            "blood_pressure_diastolic","blood_glucose"
        ]

class ParametersAfterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ParametersAfter
        fields = [
            "id","temperature","respiratory_rate","heartbite",
            "saturation","pulse",
            "blood_pressure_systolic","blood_pressure_diastolic",
            "blood_glucose"
        ]

class CommonDataSerializer(serializers.ModelSerializer):
    
    general_assessment_label = serializers.SerializerMethodField()

    class Meta:
        model = CommonData
        fields = [
            "id","complaints","anamnesis","general_assessment","сonsciousness",
            "glasgow_scale","body_position","normal_blood_pressure_systolic",
            "normal_blood_pressure_diastolic","status_localis","general_assessment_label",
        ]
    def get_general_assessment_label(self,obj):
        return obj.get_general_assessment_display()

class SkinDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SkinData
        fields = [
            "id","dry_skin","color_skin","jaundice","rash",
            "throat","tonsils","lymph_nodes","swelling"
        ]


class AirDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AirData
        fields = [
            "id","respiratory_type","wheezing","wheezing_localisation","dyspnea"
        ]

class HeartDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = HeartData
        fields = [
            "id","heart_rate_deficit","heart_tone_accent","rhythmic_tone",
            "tone_of_heart","murmur","rhythmic_pulse","characteristic_pulse"
        ]

class StomachDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StomachData
        fields = [
            "id","liver","pain_stomach","characteristic_stomach",
            "involved_in_the_act_of_breathing","formed_type_stool","regular_stool",
            "rate_stool","is_shchetkin_blumberg","is_voskresensky","is_ortner",
            "is_rovzinga","is_pasternatsky","is_sitkovsky","is_obraztsova","is_murphy"
        ]

class NervousDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NervousData
        fields = [
            "id","behaviour","reaction_to_light","pupils_of_the_eyes",
            "anisocoria","nystagmus","focal_signs","speech","none_symptoms",
            "nuchal_rigidity","is_kernig_symptom","is_brudzinski_symptom",
            "paralysis","sensitive"
        ]

class UrinaryDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UrinaryData
        fields = [
            "id","kidney_punch","characteristic_urine","with_inclusions",
            "with_sediment","painless_urination","characteristic_urination",
        ]

class ECGDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ECGData
        fields = [
            "id","ecg_before","ecg_after",
        ]

class AIDDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AIDData
        fields = [
            "id","aid","aid_effect"
        ]

class MKBSerializer(serializers.ModelSerializer):
    class Meta:
        model = MKB
        fields = ['id', 'code']

class DiagnosisDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DiagnosisData
        fields = [
           "id", "diagnosis","mkb",
        ]


class CardListSerializer(serializers.ModelSerializer):
    doctor = UserSerializer(source="doctor_id.profile", read_only=True)
    patient = PatientSerializer(source='patient_id',read_only=True)

    class Meta:
        model = Card
        fields = [
            'id', 'doctor_id', 'doctor', 'patient_id', 'patient', "address",
            'crew', 'cause', 'status', 'diagnosis_data'
        ]
    

class CardDetailSerializer(serializers.ModelSerializer):
    doctor = UserSerializer(source='doctor_id.profile', read_only=True)
    patient = PatientSerializer(source='patient_id',read_only=True)

    datetime_data = DateTimeDataSerializer(read_only=True)
    common_data = CommonDataSerializer(read_only=True)
    parameters_before_data = ParametersBeforeSerializer(read_only=True)
    parameters_after_data = ParametersAfterSerializer(read_only=True)
    skin_data = SkinDataSerializer(read_only=True)
    air_data = AirDataSerializer(read_only=True)
    heart_data = HeartDataSerializer(read_only=True)
    stomach_data = StomachDataSerializer(read_only=True)
    nervous_data = NervousDataSerializer(read_only=True)
    urinary_data = UrinaryDataSerializer(read_only=True)
    ecg_data = ECGDataSerializer(read_only=True)
    aid_data = AIDDataSerializer(read_only=True)
    diagnosis_data = DiagnosisDataSerializer(read_only=True)

    class Meta:
        model = Card
        fields = [
            'id', 'doctor_id', 'doctor', 'patient_id', 'patient', 
            'crew', 'cause', 'status', 'address',
            
            # Связанные данные
            'datetime_data', 'common_data', 'parameters_before_data',
            'skin_data', 'air_data', 'heart_data', 'stomach_data',
            'nervous_data', 'urinary_data', 'ecg_data', 'aid_data',
            'parameters_after_data', 'diagnosis_data'
        ]

class CardCreateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    surname = serializers.CharField(write_only=True)
    date_of_birth = serializers.DateField(write_only=True)
    address = serializers.CharField(write_only=True, required=False, allow_blank=True)

    patient_data = PatientSerializer(read_only=True)
    datetime_data = DateTimeDataSerializer(read_only=True)
    common_data = CommonDataSerializer(read_only=True)
    parameters_before_data = ParametersBeforeSerializer(read_only=True)
    parameters_after_data = ParametersAfterSerializer(read_only=True)
    skin_data = SkinDataSerializer(read_only=True)
    air_data = AirDataSerializer(read_only=True)
    heart_data = HeartDataSerializer(read_only=True)
    stomach_data = StomachDataSerializer(read_only=True)
    nervous_data = NervousDataSerializer(read_only=True)
    urinary_data = UrinaryDataSerializer(read_only=True)
    ecg_data = ECGDataSerializer(read_only=True)
    aid_data = AIDDataSerializer(read_only=True)
    diagnosis_data = DiagnosisDataSerializer(read_only=True)

    class Meta:
        model = Card
        fields = [
            'id', 'doctor_id', 'patient_id', 
            'first_name', 'last_name', 'surname', 'date_of_birth', 'address',
            'crew', 'cause', 'status', 'patient_data',
            'datetime_data', 'common_data', 'parameters_before_data',
            'skin_data', 'air_data', 'heart_data', 'stomach_data',
            'nervous_data', 'urinary_data', 'ecg_data', 'aid_data',
            'parameters_after_data', 'diagnosis_data'
        ]

        read_only_fields = ['id']

    def create(self,validated_data):
        
        patient_data = {
            'first_name': validated_data.pop('first_name'),
            'last_name': validated_data.pop('last_name'),
            'surname': validated_data.pop('surname'),
            'date_of_birth': validated_data.pop('date_of_birth'),
        }
        patient, _ = Patient.objects.get_or_create(**patient_data)
        print(patient, _)
        validated_data['patient_id'] = patient
        datetime_data = validated_data.pop('datetime_data', None)
        common_data = validated_data.pop('datetime_data', None)
        parameters_before_data = validated_data.pop('parameters_before_data', None)
        parameters_after_data = validated_data.pop('parameters_after_data', None)
        skin_data = validated_data.pop('skin_data', None)
        air_data = validated_data.pop('air_data', None)
        heart_data = validated_data.pop('heart_data', None)
        stomach_data = validated_data.pop('stomach_data', None)
        nervous_data = validated_data.pop('nervous_data', None)
        urinary_data = validated_data.pop('urinary_data', None)
        ecg_data = validated_data.pop('ecg_data', None)
        aid_data = validated_data.pop('aid_data', None)
        diagnosis_data = validated_data.pop('diagnosis_data', None)

        card = Card.objects.create(**validated_data)

        if datetime_data:
            DateTimeData.objects.create(card=card,**datetime_data)
        else:
            DateTimeData.objects.create(card=card,date_card=timezone.now().date())
        
        if common_data:
            CommonData.objects.create(card=card,**common_data)
        else:
            CommonData.objects.create(card=card)
        
        if parameters_before_data:
            ParametersBefore.objects.create(card=card,**parameters_before_data)
        else:
            ParametersBefore.objects.create(card=card)
        
        if parameters_after_data:
            ParametersAfter.objects.create(card=card,**parameters_after_data)
        else:
            ParametersAfter.objects.create(card=card)
        
        if skin_data:
            SkinData.objects.create(card=card,**skin_data)
        else:
            SkinData.objects.create(card=card)
        
        if air_data:
            AirData.objects.create(card=card, **air_data)
        else:
            AirData.objects.create(card=card)
        
        if heart_data:
            HeartData.objects.create(card=card, **heart_data)
        else:
            HeartData.objects.create(card=card)
        
        if stomach_data:
            StomachData.objects.create(card=card, **stomach_data)
        else:
            StomachData.objects.create(card=card)
        
        if nervous_data:
            NervousData.objects.create(card=card, **nervous_data)
        else:
            NervousData.objects.create(card=card)
        
        if urinary_data:
            UrinaryData.objects.create(card=card, **urinary_data)
        else:
            UrinaryData.objects.create(card=card)
        
        if ecg_data:
            ECGData.objects.create(card=card, **ecg_data)
        else:
            ECGData.objects.create(card=card)
        
        if aid_data:
            AIDData.objects.create(card=card, **aid_data)
        else:
            AIDData.objects.create(card=card)
                
        if diagnosis_data:
            
            DiagnosisData.objects.create(card=card, **diagnosis_data)
        else:
            DiagnosisData.objects.create(card=card)
        
        return card

class CardUpdateSerializer(serializers.ModelSerializer):
    doctor = UserSerializer(source='doctor_id.profile')
    patient = PatientSerializer(source='patient_id')
    datetime_data = DateTimeDataSerializer(required = False)
    common_data = CommonDataSerializer(required = False)
    parameters_before_data = ParametersBeforeSerializer(required = False)
    parameters_after_data = ParametersAfterSerializer(required = False)
    skin_data = SkinDataSerializer(required = False)
    air_data = AirDataSerializer(required = False)
    heart_data = HeartDataSerializer(required = False)
    stomach_data = StomachDataSerializer(required = False)
    nervous_data = NervousDataSerializer(required = False)
    urinary_data = UrinaryDataSerializer(required = False)
    ecg_data = ECGDataSerializer(required = False)
    aid_data = AIDDataSerializer(required = False)
    diagnosis_data = DiagnosisDataSerializer(required = False)

    class Meta:
        model = Card
        fields = [
            'id', 'doctor_id', 'doctor', 'patient_id', 'patient', 
            'crew', 'cause', 'status', 'address',
            
            # Связанные данные
            'datetime_data', 'common_data', 'parameters_before_data',
            'skin_data', 'air_data', 'heart_data', 'stomach_data',
            'nervous_data', 'urinary_data', 'ecg_data', 'aid_data',
            'parameters_after_data', 'diagnosis_data'
        ]
    
    def update(self,instance,validated_data):

        patient_data = validated_data.pop('patient_id', None)
        if patient_data:
        # Получаем или создаем экземпляр Patient
            patient, created = Patient.objects.update_or_create(
            id=instance.patient_id.id if instance.patient_id else None,
            defaults=patient_data
        )
            instance.patient_id = patient
        else: 
            pass
        for attr, value in validated_data.items():
            if attr not in [
            'datetime_data', 'common_data', 'parameters_before_data',
            'skin_data', 'air_data', 'heart_data', 'stomach_data',
            'nervous_data', 'urinary_data', 'ecg_data', 'aid_data',
            'parameters_after_data', 'diagnosis_data', 'patient'
            ]:
                setattr(instance,attr,value)
        instance.save()
        related_serializers = {
            "patient": Patient,
            'datetime_data':DateTimeData, 
            'common_data': CommonData, 
            'parameters_before_data': ParametersBefore,
            'skin_data': SkinData, 
            'air_data': AirData, 
            'heart_data': HeartData, 
            'stomach_data': StomachData,
            'nervous_data': NervousData, 
            'urinary_data': UrinaryData, 
            'ecg_data': ECGData,
            'aid_data': AIDData,
            'parameters_after_data': ParametersAfter, 
            'diagnosis_data':DiagnosisData
        }

        for field,model in related_serializers.items():
            if field in validated_data:
                model.objects.update_or_create(card=instance,defaults=validated_data[field])
        

        return instance