from datetime import time, date, datetime, timedelta
from rest_framework import viewsets, generics
from rest_framework import status
from rest_framework.response import Response
from estabelecimentos.models import Agenda, Estabelecimento, Servico, Horarios
from django.core.exceptions import ObjectDoesNotExist
from .serializers import AgendaSerializer, EstabelecimentoSerializer, HorarioSerializer, ServicoSerializer
from users.models import Proprietario
from estabelecimentos.utils import get_horario_termino


class EstabelecimentoViewSet(viewsets.ModelViewSet):
    queryset = Estabelecimento.objects.all()
    serializer_class = EstabelecimentoSerializer
    filterset_fields = ['proprietario']
    search_fields = ['nome', 'cidade', 'bairro', 'rua']

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            user = request.user
            data['proprietario'] = Proprietario.objects.get(
                user__id=user.id).id
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except ObjectDoesNotExist:
            return Response({'error': 'User is not an owner'}, status=status.HTTP_401_UNAUTHORIZED)


class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
    filterset_fields = ['estabelecimento']
    search_fields = ['nome', 'descricao']


class HorarioCreate(generics.ListCreateAPIView):
    queryset = Horarios.objects.all()
    serializer_class = HorarioSerializer
    filterset_fields = ['agenda']

    def create(self, request, *args, **kwargs):
        data = request.data
        data['agenda'] = Agenda.objects.get(
            estabelecimento=data.pop('estabelecimento')).id
        data['cliente'] = request.user.id
        data['horario_termino'] = get_horario_termino(
            data['data'], data['horario'], data['servico'])

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.is_valid_horario()
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        user = self.request.user
        queryset.filter(cliente=user)
        return queryset


class HorarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Horarios.objects.all()
    serializer_class = HorarioSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        data = request.data
        data['horario_termino'] = get_horario_termino(
            data.get('data') or instance.data,
            data.get('horario') or instance.horario,
            data.get('servico') or instance.servico)

        serializer = self.get_serializer(
            instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class AgendaList(generics.ListAPIView):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    filterset_fields = ['estabelecimento']
