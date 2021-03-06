from django.contrib.auth.models import User
from rest_framework import serializers
from users.models import Proprietario


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'email', 'password']

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user


class UserChangePasswordSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['password']

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('password'))
        return instance


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'email']


class ProprietarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proprietario
        fields = '__all__'
