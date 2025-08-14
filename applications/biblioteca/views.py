from django.shortcuts import render
from django.views.generic import ListView
from .models import Author

class ListaAuthors(ListView):
    template_name = "biblioteca/lista_autores.html"
    queryset = Author.objects.all()
    context_object_name = "autores"