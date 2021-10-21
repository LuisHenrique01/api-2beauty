from rest_framework import viewsets, permissions
from estabelecimentos.models import Estabelecimento
from .serializers import EstabelecimentoSerializer


class EstabelecimentoViewSet(viewsets.ModelViewSet):
    queryset = Estabelecimento.objects.all()
    serializer_class = EstabelecimentoSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ['user']
    search_fields = ['nome', 'cidade', 'bairro', 'rua']
