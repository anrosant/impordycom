# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from .models import Usuario

def index(request):
    template = loader.get_template('impordycon/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
def cerrarSesion(request):
    usuario = Usuario.objects.get(nombreUsu=request.user.username)
    usuario.online = True
    usuario.save()
    logout(request)
    return redirect('impordycon:login')
def adminPerfil(request):
    template = loader.get_template('impordycon/index.html')
    try:
        usuario = Usuario.objects.get(nombreUsu=request.user.username)
    except Usuario.DoesNotExist:
        usuario = None
    if usuario is not None:
        usuarioValido = usuario.nombreUsu
    else:
        return redirect('impordycon:login')

    context = {
        'usuario': usuarioValido,
    }
    return HttpResponse(template.render(context, request))
def loginUser(request):
    template = loader.get_template('impordycon/login.html')
    if(request.method == 'POST'):
        nombre = request.POST['usuario']
        clave = request.POST['password']
        user = authenticate(username=nombre, password=clave)
        if user is not None:
            usuario = Usuario.objects.get(nombreUsu=nombre);
            if usuario is not None:
                login(request, user)
                usuario.online = True
                usuario.save()
                if usuario.tipo == "administrador":
                    return redirect('impordycon:administrador')
        else:
            notice='Ingreso Invalido'
    else:
        notice='none'
    context = {
        'notice':notice
    }
    return HttpResponse(template.render(context, request))
