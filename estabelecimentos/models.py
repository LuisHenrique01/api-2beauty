from django.db import models
from users.models import Proprietario
from django.contrib.auth.models import User
# Create your models here.


class Estabelecimento(models.Model):

    proprietario = models.ForeignKey(
        Proprietario, on_delete=models.CASCADE, related_name='estabelecimentos')
    nome = models.CharField('Nome', max_length=250)
    cnpj = models.CharField('CNPJ', max_length=25)
    cidade = models.CharField('Cidade', max_length=250)
    bairro = models.CharField('bairro', max_length=250)
    rua = models.CharField('Rua', max_length=250)
    numero = models.CharField('Numero', max_length=250)
    cep = models.CharField('CEP', max_length=15)
    horario_inicio = models.TimeField()
    horario_final = models.TimeField()
    telefone = models.CharField('CEP', max_length=50)
    latitude = models.CharField('Latitude', max_length=100)
    longitude = models.CharField('Longitude', max_length=100)
    data_cadastro = models.DateField('Data cadastro', auto_now_add=True)

    def __str__(self):
        return self.nome


class Servico(models.Model):

    nome = models.CharField(max_length=250)
    descricao = models.TextField(blank=True, null=True)
    preco = models.FloatField()
    duracao = models.IntegerField()

    def __str__(self):
        return self.name


class Horarios(models.Model):

    cliente = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='clientes')
    servico = models.ForeignKey(
        Servico, on_delete=models.CASCADE, related_name='servicos')
    inicio = models.DateTimeField()
    fim = models.DateTimeField()

    class Meta:
        verbose_name = "Horarios"
        verbose_name_plural = "Horarios"

    def __str__(self):
        return f'{self.cliente}'


class Agenda(models.Model):

    estabelecimento = models.OneToOneField(
        Estabelecimento, on_delete=models.CASCADE)
    horarios = models.ForeignKey(
        Horarios, on_delete=models.CASCADE, related_name='horarios')

    def __str__(self):
        return f'{self.estabelecimento}'
