from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from estabelecimentos.models import Estabelecimento
from .serializers import EstabelecimentoSerializer
from users.models import Proprietario

class EstabelecimentoViewSet(viewsets.ModelViewSet):
    queryset = Estabelecimento.objects.all()
    serializer_class = EstabelecimentoSerializer
    filterset_fields = ['user']
    search_fields = ['nome', 'cidade', 'bairro', 'rua']

    def create(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        data['proprietario'] = Proprietario.objects.get(user=user)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
