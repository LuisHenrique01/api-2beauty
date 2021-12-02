from django.urls import path, include
from .api.viewsets import EstabelecimentoViewSet, ServicoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('estabelecimento', EstabelecimentoViewSet)
# router.register('agenda', AgendaViewSet)
router.register('servico', ServicoViewSet)

urlpatterns = [
    path('', include(router.urls))
]
