from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from proyectoCiex import index

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index.index, name = 'index'),
    url(r'^Chilpancingo/cafeteria/' ,include('cafeteria.urls')),
    url(r'^usuario/',include('registro.urls') , name = 'registro_usuario'),
    url(r'^Chilpancingo/libreria/', include('libreria.urls')),
    url(r'^Chilpancingo/comercializadora/', include('comercializadora.urls')),
    url(r'^Chilpancingo/control/', include('control.urls')),
    url(r'^Puebla/cafeteria/' ,include('cafeteria_puebla.urls')),
    url(r'^Puebla/libreria/', include('libreria_puebla.urls')),
    url(r'^Puebla/control/', include('control_puebla.urls'))
)

if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',(r'^media/(?P<path>.*)','serve', {'document_root': settings.MEDIA_ROOT}), )