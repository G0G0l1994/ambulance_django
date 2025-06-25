from rest_framework import serializers
from django.contrib.auth.models import User
from user.models import Profile



class UserCreateSerializer(serializers.ModelSerializer):
    surname: str = serializers.CharField(write_only = True)
    role: str = serializers.ChoiceField(choices=Profile.ROLE_CHOICE, write_only = True)

    class Meta:
        model = User
        fields = ['id',
            'username',
            'first_name',
            'last_name',
            'surname',
            'role',
            'password',
            'email'
        ]
        extra_kwargs = {
            'email': {'required': True},
        }

    def validate_email(self,value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Email already exist')
        return True

    def create(self,validated_data):
        role = validated_data.pop("role")
        surname = validated_data.pop("surname")
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user,
                                      surname = surname,
                                      role = role)
        return user

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')

    class Meta:
        model = Profile
        fields = ['id',
            'first_name',
            'surname',
            'last_name',
            'role',
            'email',
            'username',
            'uuid_session',
        ]
