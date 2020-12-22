from django.db import models

class Paciente(models.Model):
    cpf = models.CharField(max_length=11, primary_key=True)
    nome = models.CharField(max_length=50)
    cartao_sus = models.CharField(max_length=15)
