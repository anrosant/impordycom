from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

app_name = 'impordyconApp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.loginUser, name='login'),
    url(r'^administrador/', views.adminPerfil, name='administrador'),
    url(r'^cerrarSesion/$', views.cerrarSesion, name='cerrarSesion'),
]
