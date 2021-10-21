from django.db import models
from django.contrib.auth.models import User


class Proprietario(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='proprietario')
    cpf = models.CharField('CPF', max_length=20)
    

    class Meta:
        verbose_name = "Proprietário"
        verbose_name_plural = "Proprietários"

    def __str__(self):
        return self.user.first_name
