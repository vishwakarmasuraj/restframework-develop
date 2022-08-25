from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ["name", "email", "password", "mobile", "address", "pin_code", "city", "state"]

