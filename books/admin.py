from django.contrib import admin
from .models import Books, Genres

# Register your models here.

class BooksAdmin(admin.ModelAdmin):
    list_display = (
        'isbn',
        'author',
        'title',
        'binding',
        'genres',
        'price',
        'sale',
        'image',
    )
    ordering = ('isbn',)

class GenresAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Books, BooksAdmin)
admin.site.register(Genres, GenresAdmin)
