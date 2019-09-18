__author__ = 'RubenMurga'

from django.conf.urls import patterns, include, url
from registro import views, busquedas_ajax


urlpatterns = patterns('',
    url(r'^registro/$', views.registro_usuario, name = 'register_user'),
    url(r'^completar_registro/$', views.terminar_registro, name='complete_your_data'),
    url(r'^logout', views.cerrar_sesion, name = 'cerrar_sesion'),
    url(r'^buscar-usuario/$',busquedas_ajax.buscar_usuario),
    url(r'^ayuda/$', views.ayuda, name = 'registro_ayuda'),
)