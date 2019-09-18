# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from registro.models import UserProfile
from registro.registro_forms import UserProfileForm, UserForm
from django.contrib.auth.decorators import login_required
from registro.models import UserProfile


def registro_usuario(request):
    dic_context = {}
    if request.method == 'POST':
        username_form = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        user = authenticate(username = username_form, password = password1)
        if user is not None:
            resultado = "Lo siento, las contraseñas no coinciden o el nombre de usuario ya existe"
            rest = "alert-danger"
            imagen = "mal.png"
        else:
            if password1 == password2:
                if int(request.POST.get('codigo')) == 3897654328:
                    User.objects.create_user(username_form, 'email', password1)
                    authenticate(user=username_form, password = password1)
                    resultado = "Se ha creado tu cuenta satisfactoriamente"
                    rest = "alert-success"
                    imagen = "bien.png"
                    crear = UserProfile()
                    user = User.objects.get(username=username_form)
                    crear.user = user
                    crear.save()
                else:
                    resultado = "No te puedes registrar"
                    rest = "alert-danger"
                    imagen = "mal.png"

            else:
                resultado = "Lo siento, las contraseñas no coinciden o el nombre de usuario ya existe"
                rest = "alert-danger"
                imagen = "mal.png"
        dic_context['mensaje'] = resultado
        dic_context['clase'] = rest
        dic_context['imagen'] = imagen

        return render(request, 'usuario/respuesta.html', dic_context)
    return render(request, 'usuario/registro_usuario.html',request)
@login_required
def terminar_registro(request):
    dict_context = {}
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            if int(request.POST.get('codigo')) == 9765436383:
                user = User.objects.get(username = request.user.username)
                user.first_name = request.POST.get('first_name')
                user.last_name = request.POST.get('last_name')
                user.email = request.POST.get('email')
                user.save()
                profile = UserProfile.objects.get(user_id = user.id)
                if 'picture' in request.FILES:
                    profile.picture = request.FILES['picture']
                profile.belongs_to = request.POST.get('belongs_to')
                profile.completed_data = 1
                profile.save()
                redireccion = request.POST.get('belongs_to').lower()
                if redireccion == 'administrador':
                    return HttpResponseRedirect('/control/inicio/')
                else:
                    redireccion =  '/'+redireccion+'/inicio'
                return HttpResponseRedirect(redireccion)
            else:
                dict_context['user_form'] = user_form
                dict_context['profile_form'] = profile_form
                return render(request, 'usuario/complete_your_data.html',dict_context)
        else:
            dict_context['user_form'] = user_form
            dict_context['profile_form'] = profile_form
            return render(request, 'usuario/complete_your_data.html',dict_context)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm
        dict_context['user_form'] = UserForm()
        dict_context['profile_form'] = UserProfileForm
    return render(request, 'usuario/complete_your_data.html',dict_context)
@login_required
def cerrar_sesion(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def ayuda(request):
    dic_context = {}
    dic_context['usuario'] = UserProfile.objects.get(user = request.user)

    return render(request,'ayuda/ayuda.html', dic_context)
