from django.conf.urls import url, include
from django.contrib import admin
from impordyconApp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^impordycom/', include('impordyconApp.urls')),
]
