from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

app_name = 'impordyconApp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
