# -*- coding: utf-8 -*-

__author__ = 'RubenMurga'
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from registro.models import UserProfile

def index(request):
    if request.method == "POST":
        context_dict = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                datos = UserProfile.objects.get(user_id = user)
                if datos.completed_data == 0:
                    return HttpResponseRedirect('usuario/completar_registro/')
                else:
                    if datos.sucursal == 0:
                        if datos.belongs_to == "Cafeteria":
                            return HttpResponseRedirect('Chilpancingo/cafeteria/inicio/')
                        elif datos.belongs_to == "Libreria":
                            return HttpResponseRedirect('Chilpancingo/libreria/inicio/')
                        elif datos.belongs_to == "Administrador":
                            return HttpResponseRedirect('Chilpancingo/control/inicio/')
                    elif datos.sucursal==1:
                        if datos.belongs_to == "Cafeteria":
                            return HttpResponseRedirect('Puebla/cafeteria/inicio/')
                        elif datos.belongs_to == "Libreria":
                            return HttpResponseRedirect('Puebla/libreria/inicio/')
                        elif datos.belongs_to == "Administrador":
                            return HttpResponseRedirect('Puebla/control/inicio/')

            else:
                context_dict['mensaje'] = "tu cuenta ha sido deshabilitada"
                context_dict['clase'] = "alert-warning"
                context_dict['imagen'] = "cuidado.png"
                return render(request, 'usuario/respuesta.html', context_dict)
        else:
            context_dict['mensaje'] = "usuario y/o contraseña incorrecta"
            context_dict['clase'] = "alert-danger"
            context_dict['imagen'] = "mal.png"
            return render(request, 'usuario/respuesta.html', context_dict)
    return render(request, 'index.html')


