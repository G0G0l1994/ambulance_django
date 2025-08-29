from django.contrib.auth.models import User
from rest_framework import serializers

from user.models import Profile, Crew


class UserCreateSerializer(serializers.ModelSerializer):
    surname = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=Profile.ROLE_CHOICE, write_only=True)
    passwordConfirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "surname", "role", "password", "passwordConfirm", "email"]
        extra_kwargs = {
            "email": {"required": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exist")
        return value

    def validate(self, attrs):
        if attrs["password"] != attrs["passwordConfirm"]:
            raise serializers.ValidationError({"password": "Password fields didn't match"})
        return attrs

    def create(self, validated_data):
        role = validated_data.pop("role")
        surname = validated_data.pop("surname")
        validated_data.pop('passwordConfirm')
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user, surname=surname, role=role)
        return user


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='user.id')
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.EmailField(source='user.email')
    is_online = serializers.BooleanField()
    surname = serializers.CharField()
    role = serializers.CharField()
    full_name_display = serializers.SerializerMethodField(allow_null=True) 

    class Meta:
        model = Profile
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email', # из User
            'surname', 'role', 'is_online',# из Profile
            'full_name_display'
                
        ]
    
    
    
    def get_full_name_display(self, obj):
        return obj.full_name()

class CrewSerializer(serializers.ModelSerializer):
    crew_number = serializers.CharField(allow_null=True)
    main = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), allow_null =True, required =False)
    secondary = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), allow_null =True, required =False)
    main_display = serializers.SerializerMethodField(allow_null=True)
    secondary_display = serializers.SerializerMethodField(allow_null=True)

    class Meta:
        model = Crew
        fields = [
            'id','crew_number', 'main', 'secondary', 'main_display', 'secondary_display'
        ]

    def _get_full_name(self, user):
        if user and hasattr(user, 'profile'):
            return user.profile.full_name()
        return None
    
    def get_main_display(self, obj):
        return self._get_full_name(obj.main)
    
    def get_secondary_display(self, obj):
        return self._get_full_name(obj.secondary)
    