from django.db import models
from django.contrib.auth.models import User


class ProprietarioModel(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField('CPF', max_length=15)
    telefone = models.CharField('Telefone', max_length=15)
    