from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Estabelecimento(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='estabelecimentos')
    nome = models.CharField('Nome', max_length=250)
    cidade = models.CharField('Cidade', max_length=250)
    bairro = models.CharField('bairro', max_length=250)
    rua = models.CharField('Rua', max_length=250)
    numero = models.CharField('Numero', max_length=250)
    cep = models.CharField('CEP', max_length=15)
    telefone = models.CharField('CEP', max_length=50)
    latitude = models.CharField('Latitude', max_length=100)
    longitude = models.CharField('Longitude', max_length=100)
    data_cadastro = models.DateField('Data cadastro', auto_now_add=True)

    def __str__(self):
        return self.nome
