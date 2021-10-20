from django.urls import path, include
from .api.viewsets import EstabelecimentoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', EstabelecimentoViewSet)

urlpatterns = [
    path('', include(router.urls))
]
