from django.contrib import admin
from django.urls import path
from fluxogramaapp.views import fluxograma

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", fluxograma, name="inicio"),
    path("fluxograma/", fluxograma, name="fluxograma"),
]
