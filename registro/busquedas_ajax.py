__author__ = 'RubenMurga'
import json
from django.http import HttpResponse
from django.contrib.auth.models import User

def buscar_usuario(request):
    if request.method == 'GET':
        usuario = request.GET['usuario']
        busqueda = User.objects.get(username = usuario)
    return HttpResponse(json.dumps({'nombre':busqueda.username}),content_type = 'aplication/json')

