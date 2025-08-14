from django.db import models


class Author(models.Model):
    name = models.CharField("Nombres", max_length=80)
    nacionality = models.CharField("Nacionalidad", blank=True, max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField("Título", max_length=150)
    resume = models.TextField("Resumen", blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title