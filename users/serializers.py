"""
Serializer for registering a new user.
This serializer handles the creation of a new Django
User instance, requiring a username, email, and password.
The password field is write-only to ensure it is not exposed in API responses.
Classes:
    RegisterSerializer: Inherits from serializers.
    ModelSerializer to provide validation and
    creation logic for user registration.
Methods:
    create(validated_data): Creates and returns a
    new User instance using the provided validated data.
"""

from django.contrib.auth.models import User

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """

    class Meta:
        """
        Meta class for UserSerializer.
        Specifies the model and fields to be used in the serializer.
        """

        model = User
        fields = ("id", "username", "email", "is_staff")


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for registering a new user.
    Fields:
        username (str): The username for the new user.
        email (str): The email address for the new user.
        password (str): The password for the new user (write-only).
    Methods:
        create(validated_data):
            Creates and returns a new User instance using the provided validated data.
    """

    password = serializers.CharField(write_only=True)

    class Meta:
        """
        Meta class for RegisterSerializer.
        Specifies the model and fields to be used in the serializer.
        """

        model = User
        fields = ("username", "email", "password")

    def create(self, validated_data):
        """
        Creates and returns a new User instance using the provided validated data.

        Args:
            validated_data (dict): A dictionary containing user
            information with keys 'username', 'email', and 'password'.

        Returns:
            User: The newly created User instance.
        """
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user
