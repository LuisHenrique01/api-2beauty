from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from users.models import Proprietario
from .serializers import UserCreateSerializer, UserDetailSerializer, UserChangePasswordSerializer, ProprietarioSerializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]


class UserChangePassword(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserChangePasswordSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class GetUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    filterset_fields = ['username', 'email']


class ProprietarioViewSet(ModelViewSet):
    queryset = Proprietario.objects.all()
    serializer_class = ProprietarioSerializer
    
    def create(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        data['user'] = User.objects.get(user=user)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)