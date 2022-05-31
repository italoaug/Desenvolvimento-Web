from django.db import models

class Membros(models.Model):
  nome = models.CharField(max_length=255)
  sobrenome = models.CharField(max_length=255)

