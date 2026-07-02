from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def validate_username(self, value):
        if not value.strip():
            raise serializers.ValidationError("Username cannot be empty.")
        return value

    def create(self, data):
        return User.objects.create_user(**data)
