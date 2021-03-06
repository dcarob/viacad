
from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve


urlpatterns = [
   url(r'^$',views.index,name='index'),
   url(r'^login/$',views.login,name='login'),
   url(r'^editarprofesor/$',views.editarprofesor,name='editarprofesor'),
   url(r'^logout/$',views.logout,name='logout'),
   url(r'^perfilprof/$',views.perfilprof,name='perfilprof'),
   url(r'^editaralumno/$',views.editaralumno,name='editaralumno'),
   url(r'^perfilalum/$',views.perfilalum,name='perfilalum'),
   url(r'^registroProfesores/$', views.registroProfesores,name='registroProfesores' ),
   url(r'^registroAlumnos/$', views.registroAlumnos,name='registroAlumnos' ),
   url(r'^buscarprof/$', views.buscarprof,name='buscarprof' ),
   url(r'^elegido/$', views.registroSolicitud,name='elegido' ),
   url(r'^registroAlumnos/buscarprof/elegido/buscarprof/$', views.buscarprof,name='buscarprof' ),
   url(r'^elegido/$', views.registroSolicitud,name='elegido' )
   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
