from django.contrib.auth.models import User
from rest_framework import serializers

from user.models import Profile


class UserCreateSerializer(serializers.ModelSerializer):
    surname: str = serializers.CharField(write_only=True)
    role: str = serializers.ChoiceField(choices=Profile.ROLE_CHOICE, write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "surname", "role", "password", "email"]
        extra_kwargs = {
            "email": {"required": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exist")
        return value

    def validete_password(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Password fields didn't match"})
        return attrs

    def create(self, validated_data):
        role = validated_data.pop("role")
        surname = validated_data.pop("surname")
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user, surname=surname, role=role)
        return user

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "username": instance.username,
            "first_name": instance.first_name,
            "surname": instance.profile.surname,
            "last_name": instance.last_name,
            "role": instance.profile.role,
        }


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.CharField(source="user.email")

    class Meta:
        model = Profile
        fields = [
            "id",
            "first_name",
            "surname",
            "last_name",
            "role",
            "email",
            "username",
            "uuid_session",
        ]
