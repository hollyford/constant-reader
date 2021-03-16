from django.shortcuts import render
from .models import Books

# Create your views here.

def all_books(request):
    """ A view to show all books, including sorting and searches """

    books = Books.objects.all()

    context = {
        'books': books,
    }

    return render(request, 'books/books.html', context)