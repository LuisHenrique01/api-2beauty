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

    def is_valid_horario(self):
        validated_data = self.validated_data
        agenda = Horarios.objects.filter(
            agenda=validated_data['agenda'],
            cliente=validated_data['cliente'],
            servico=validated_data['servico'],
            data=validated_data['data'],
            horario__gte=validated_data['horario'],
            horario_termino__lte=validated_data['horario_termino']
        )
        estabelecimento = Estabelecimento.objects.get(
            agenda=validated_data['agenda'])
        if estabelecimento.horario_inicio < validated_data['horario'] \
                or estabelecimento.horario_final >= validated_data['horario']:
            raise serializers.ValidationError(
                {'error': 'Fora do horário de atendimento!'})
        if len(agenda) >= validated_data['servico'].qtd_atendentes:
            raise serializers.ValidationError(
                {'error': 'Horário indisponível!'})
        return True


class AgendaSerializer(serializers.ModelSerializer):
    estabelecimento = EstabelecimentoSerializer()
    horarios = HorarioSerializer(many=True)

    class Meta:
        model = Agenda
        fields = ['estabelecimento', 'horarios']
