from django.urls import path, include

from estabelecimentos.views import Docs
from .api.viewsets import AgendaList, AgendaList, EstabelecimentoViewSet, HorarioCreate, HorarioDetail, ServicoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('estabelecimento', EstabelecimentoViewSet)
router.register('servico', ServicoViewSet)

urlpatterns = [
    path("docs/", Docs.as_view(), name="dosc"),
    path("", include(router.urls)),
    path("horario/", HorarioCreate.as_view()),
    path("agenda/", AgendaList.as_view()),
    path("horario/<int:pk>/", HorarioDetail.as_view())
]
