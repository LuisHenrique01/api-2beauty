from django.urls import path
from .api.viewsets import UserCreate, UserDetail

urlpatterns = [
    path('', UserCreate.as_view()),
    path('<int:pk>/', UserDetail.as_view())
]