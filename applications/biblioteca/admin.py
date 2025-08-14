from django.contrib import admin

from .models import Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "nacionality", "id")
    search_fields = ("name", "nacionality")

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "resume", "author", "id")
    search_fields = ("title", "author__name")
    list_filter = ("author",)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)