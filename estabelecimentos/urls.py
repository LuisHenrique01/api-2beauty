from django.urls import path, include

from .api.viewsets import AgendaList, EstabelecimentoViewSet, HorarioCreate, HorarioDetail, ServicoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('estabelecimento', EstabelecimentoViewSet)
router.register('servico', ServicoViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("horario/", HorarioCreate.as_view()),
    path("agenda/", AgendaList.as_view()),
    path("horario/<int:pk>/", HorarioDetail.as_view())
]
