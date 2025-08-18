from django.urls import path

from . import views

app_name = "biblioteca_app"

urlpatterns = [
    path("", views.ListaAuthors.as_view(), name="lista_autores"),
    path("libros-autor/<int:pk>/", views.ListaBooksByAuthor.as_view(), name="lista_libros"),
    path("autor/add/", views.AddAuthor.as_view(), name="autor_add"),
]