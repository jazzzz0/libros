from django.urls import path

from . import views

app_name = "biblioteca_app"

urlpatterns = [
    path("autores/", views.ListaAuthors.as_view(), name="lista_autores"),
]