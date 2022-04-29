from django.db import models

class Usuarios(models.Model):
    nome_usuario = models.CharField(max_length=200)
    email_usuario = models.EmailField(max_length=200)
    password_usuario = models.CharField(max_length=200)
    confirmacao_password_usuario = models.CharField(max_length=200)
