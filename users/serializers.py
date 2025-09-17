"""
Serializers for the user app.

Includes serializers for user registration, login, and profile management.
"""

from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', "is_staff"]
