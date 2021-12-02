from django.urls import path, include
from .api.viewsets import UserCreate, UserDetail, UserChangePassword, \
    ProprietarioCreate, ProprietarioDetail

urlpatterns = [
    path('', UserCreate.as_view()),
    path('change/password/', UserChangePassword.as_view()),
    path('get/', UserDetail.as_view()),
    path("proprietario/create/", ProprietarioCreate.as_view()),
    path("proprietario/", ProprietarioDetail.as_view())
]
