from rest_framework import viewsets, generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, RegisterSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


# Registro de usuario
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
