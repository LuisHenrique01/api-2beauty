from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from users.models import Proprietario
from .serializers import UserCreateSerializer, UserDetailSerializer, UserChangePasswordSerializer, ProprietarioSerializer


class UserCreate(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]

    def get_user(self, data):
        return User.objects.get(username=data['username'])

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data_token = self.get_tokens_for_user(self.get_user(serializer.data))
        return Response(data_token, status=status.HTTP_201_CREATED, headers=headers)


class UserChangePassword(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserChangePasswordSerializer

    def get_object(self):
        obj = self.request.user
        return obj


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    def get_object(self):
        obj = self.request.user
        return obj


class ProprietarioCreate(generics.CreateAPIView):
    queryset = Proprietario.objects.all()
    serializer_class = ProprietarioSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        data['user'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ProprietarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proprietario.objects.all()
    serializer_class = ProprietarioSerializer

    def get_object(self):
        obj = Proprietario.objects.get(user=self.request.user)
        return obj
