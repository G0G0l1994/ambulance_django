from django.contrib.auth.models import User
from rest_framework import serializers

from user.models import Profile


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
    surname = serializers.CharField()
    role = serializers.CharField()

    class Meta:
        model = Profile
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email',  # из User
            'surname', 'role'  # из Profile
        ]
