from rest_framework import serializers
from django.contrib.auth.models import User
from estabelecimentos.models import Estabelecimento

class EstabelecimentoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Estabelecimento
        fields = '__all__'
