from django.urls import path
from .api.viewsets import UserCreate, UserDetail, UserChangePassword, GetUser

urlpatterns = [
    path('', UserCreate.as_view()),
    path('get/', GetUser.as_view()),
    path('change/password/<int:pk>/', UserChangePassword.as_view()),
    path('<int:pk>/', UserDetail.as_view())
]