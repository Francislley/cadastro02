# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    ramal = models.CharField(max_length=100)
    foto = models.FileField()

    def __str__(self):
        return self.nome
