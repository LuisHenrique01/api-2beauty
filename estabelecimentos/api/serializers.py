from django.db.models import fields
from rest_framework import serializers
from estabelecimentos.models import Estabelecimento, Servico


class EstabelecimentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estabelecimento
        fields = '__all__'


class ServicoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Servico
        fields = '__all__'
