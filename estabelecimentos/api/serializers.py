from rest_framework import serializers
from estabelecimentos.models import Estabelecimento, Servico, Agenda, Horarios
from users.api.serializers import UserSerializer


class EstabelecimentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estabelecimento
        fields = '__all__'

    def create(self, validated_data):
        estabelecimento = Estabelecimento.objects.create(**validated_data)
        Agenda.objects.create(estabelecimento=estabelecimento)
        return estabelecimento


class ServicoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Servico
        fields = '__all__'


class HorarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Horarios
        fields = '__all__'


class AgendaSerializer(serializers.ModelSerializer):
    horarios = HorarioSerializer()

    class Meta:
        model = Agenda
        fields = '__all__'
