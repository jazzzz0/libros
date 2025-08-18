from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Author, Book

class ListaAuthors(ListView):
    template_name = "biblioteca/lista_autores.html"
    queryset = Author.objects.all()
    context_object_name = "autores"

class ListaBooksByAuthor(ListView):
    template_name = "biblioteca/lista_libros.html"
    context_object_name = "libros"

    def get_queryset(self):
        return Book.objects.filter(author_id=self.kwargs["pk"])

class AddAuthor(CreateView):
    template_name = "biblioteca/add_author.html"
    model = Author
    fields = ["name", "nacionality"]
    success_url = "/"