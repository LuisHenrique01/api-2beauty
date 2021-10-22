from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserCreateSerializer, UserDetailSerializer, UserChangePasswordSerializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]


class UserChangePassword(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserChangePasswordSerializer
    permission_classes = [permissions.AllowAny]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.AllowAny]
