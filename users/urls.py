from django.urls import path
from .api.viewsets import UserCreate, UserDetail, UserChangePassword, \
    ProprietarioCreate, ProprietarioDetail

urlpatterns = [
    path('', UserCreate.as_view(), name='user-create'),
    path('change/password/', UserChangePassword.as_view(), name='change-password'),
    path('get/', UserDetail.as_view(), name='get-user'),
    path("proprietario/create/", ProprietarioCreate.as_view(),
         name='proprietario-create'),
    path("proprietario/", ProprietarioDetail.as_view(), name='get-proprietario')
]
