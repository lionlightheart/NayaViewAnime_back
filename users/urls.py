from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RegisterView

router = DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path("", include(router.urls)),  # CRUD de usuarios
    path("/register/", RegisterView.as_view(), name="register"),  # Registro
]
