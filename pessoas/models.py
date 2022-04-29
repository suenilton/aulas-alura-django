from django.db import models


class Pessoa(models.Model):
    nome_pessoa = models.CharField(max_length=200, blank=True)
    email_pessoa = models.CharField(max_length=200, blank=True)

    def __str__(self) -> str:
        return self.nome_pessoa