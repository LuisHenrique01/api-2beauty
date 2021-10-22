from django.contrib.auth.models import User
from rest_framework import serializers

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
        fields = ['username', 'password']

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('password'))
        return instance


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'email']

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('password'))
        return instance