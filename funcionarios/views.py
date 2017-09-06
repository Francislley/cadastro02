# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Funcionario
from django.template import loader


def get_funcionarios(request):
    all_funcionarios =  Funcionario.objects.all()
    template = loader.get_template('funcionarios/funcionarios.html')

    context = {'all_funcionarios': all_funcionarios}

    return HttpResponse(template.render(context, request))

def get_funcionario_by_name(request, funcionario_id):
    pass
