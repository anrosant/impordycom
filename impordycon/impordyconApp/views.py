# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('impordycon/index.html')
    context = {
        'usuario': "nombreUsuario",
    }
    return HttpResponse(template.render(context, request))
