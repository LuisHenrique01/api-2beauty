from django.db import models
from django.contrib.auth.models import User


class Proprietario(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField('CPF', max_length=15)
    data_nascimento = models.DateField('Data de Nascimento')
    telefone = models.CharField('Telefone', max_length=15)
    data_cadastro = models.DateField('Data cadastro', auto_now_add=True)

    def __str__(self):
        return self.user.first_name
