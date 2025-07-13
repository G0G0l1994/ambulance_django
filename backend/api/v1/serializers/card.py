from django.utils import timezone
from rest_framework import serializers

from card.models import (
    Card,Patient,DateTimeData,ParametersBefore,ParametersAfter,CommonData,
    SkinData,AirData,HeartData,StomachData,NervousData,
    UrinaryData,ECGData,AIDData,DiagnosisData)
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
    
    class Meta:
        model = DateTimeData
        fields = [
            "id","date_card","time_of_receipt","transmission_time",
            "departure_time","arrival_time","start_time_of_hospitalization",
            "time_of_arrival_at_hospital","call_end_time"
        ]

class ParametersBeforeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ParametersBefore
        fields  = [
            "id","temperature_before","respiratory_rate_before","heartbite_before",
            "saturation_before","pulse_before","blood_pressure_systolic_before",
            "blood_pressure_diastolic_before","blood_glucose_before"
        ]

class ParametersAfterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ParametersAfter
        fields = [
            "id","temperature_after","respiratory_rate_after","heartbite_after",
            "saturation_after","pulse_after",
            "blood_pressure_systolic_after","blood_pressure_diastolic_after",
            "blood_glucose_after"
        ]

class CommonDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CommonData
        fields = [
            "id","complaints","anamnesis","general_assessment","сonsciousness",
            "glasgow_scale","body_position","normal_blood_pressure_systolic",
            "normal_blood_pressure_diastolic","status_localis"
        ]

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

class DiagnosisDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DiagnosisData
        fields = [
           "id", "diagnosis","mkb",
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
            'crew', 'cause', 'status', 'status_display', 'created_at',
            
            # Связанные данные
            'datetime_data', 'common_data', 'parameters_before_data',
            'skin_data', 'air_data', 'heart_data', 'stomach_data',
            'nervous_data', 'urinary_data', 'ecg_data', 'aid_data',
            'parameters_after_data', 'diagnosis_data'
        ]

class CardCreateSerializer(serializers.ModelSerializer):
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
            'crew', 'cause', 'status',
            'datetime_data', 'common_data', 'parameters_before_data',
            'skin_data', 'air_data', 'heart_data', 'stomach_data',
            'nervous_data', 'urinary_data', 'ecg_data', 'aid_data',
            'parameters_after_data', 'diagnosis_data'
        ]

        read_only_fields = ['id']

    def create(self,validated_data):
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
            DateTimeData.objects.create(card_id=card,**datetime_data)
        else:
            DateTimeData.objects.create(card_id=card,date_card=timezone.now().date())
        
        if common_data:
            CommonData.objects.create(card_id=card,**common_data)
        else:
            CommonData.objects.create(card_id=card)
        
        if parameters_before_data:
            ParametersBefore.objects.create(card_id=card,**parameters_before_data)
        else:
            ParametersBefore.objects.create(card_id=card)
        
        if parameters_after_data:
            ParametersAfter.objects.create(card_id=card,**parameters_after_data)
        else:
            ParametersAfter.objects.create(card_id=card)
        
        if skin_data:
            SkinData.objects.create(card_id=card,**skin_data)
        else:
            SkinData.objects.create(card_id=card)
        
        if air_data:
            AirData.objects.create(card_id=card, **air_data)
        else:
            AirData.objects.create(card_id=card)
        
        if heart_data:
            HeartData.objects.create(card_id=card, **heart_data)
        else:
            HeartData.objects.create(card_id=card)
        
        if stomach_data:
            StomachData.objects.create(card_id=card, **stomach_data)
        else:
            StomachData.objects.create(card_id=card)
        
        if nervous_data:
            NervousData.objects.create(card_id=card, **nervous_data)
        else:
            NervousData.objects.create(card_id=card)
        
        if urinary_data:
            UrinaryData.objects.create(card_id=card, **urinary_data)
        else:
            UrinaryData.objects.create(card_id=card)
        
        if ecg_data:
            ECGData.objects.create(card_id=card, **ecg_data)
        else:
            ECGData.objects.create(card_id=card)
        
        if aid_data:
            AIDData.objects.create(card_id=card, **aid_data)
        else:
            AIDData.objects.create(card_id=card)
                
        if diagnosis_data:
            DiagnosisData.objects.create(card_id=card, **diagnosis_data)
        else:
            DiagnosisData.objects.create(card_id=card)
        
        return card

class CardUpdateSerializer(serializers.ModelSerializer):
    pass