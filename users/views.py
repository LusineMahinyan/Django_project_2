from rest_framework import generics
from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

from rest_framework import generics, viewsets
from .models import User
from .serializers import RegisterSerializer


# регистрация (оставляем как есть)
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


# CRUD пользователей (ЭТО ТЫ НЕ ДОБАВИЛА)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer