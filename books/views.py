from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Books, Genres
from .forms import BookForm

# Create your views here.


def all_books(request):
    """ A view to show all books, including sorting and searches """

    books = Books.objects.all()
    query = None
    genres = None
    sort = None
    direction = None


    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                books = books.annotate(lower_name=Lower('name'))
            if sortkey == 'genres':
                sortkey = 'genres__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            books = books.order_by(sortkey)

        if 'genres' in request.GET:
            genres = request.GET['genres'].split(',')
            books = books.filter(genres__name__in=genres)
            genres = Genres.objects.filter(name__in=genres)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('books'))

            queries = Q(title__icontains=query) | Q(
                description__icontains=query) | Q(author__icontains=query)
            books = books.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'books': books,
        'search_term': query,
        'current_genres': genres,
        'current_sorting': current_sorting,
    }

    return render(request, 'books/books.html', context)


def book_detail(request, book_id):
    """ A view to show individual book details """

    book = get_object_or_404(Books, pk=book_id)

    context = {
        'book': book,
    }

    return render(request, 'books/book_detail.html', context)


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added a book!')
            return redirect(reverse('add_book'))
        else:
            messages.error(request, 'Failed to add book. Please check the details and try again')
    else: 
        form = BookForm()
    template = 'books/add_book.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_book (request, book_id):
    book = get_object_or_404(Books, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the book!')
            return redirect(reverse('book_detail', args=[book.id]))
        else:
            messages.error(request, 'Failed to update the book. Please check the details and try again')
    else:
        form = BookForm(instance=book)
        messages.info(request, 'You are editing this book')

    template = 'books/edit_book.html'
    context = {
        'form': form,
        'book': book,
    }

    return render(request, template, context)
