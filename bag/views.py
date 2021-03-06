from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from books.models import Books
# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, book_id):
    """ Add a quantity of the specified product to the shopping bag """

    book = get_object_or_404(Books, pk=book_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag', {})

    if book_id in list(bag.keys()):
        bag[book_id] += quantity
        messages.success(
            request, f'{book.title} has been added to your book bag again')
    else:
        bag[book_id] = quantity
        messages.success(request, f'Added {book.title} to your book bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, book_id):
    """ adjust the quantity of the specified product to the specified amount """

    book = get_object_or_404(Books, pk=book_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[book_id] = quantity
        messages.success(
            request, f'Updated the quantity of {book.title} books in your book bag')
    else:
        bag.pop(book_id)
        messages.success(request, f'Removed {book.title} from your book bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, book_id):
    """ remove item from the shopping bag """

    try:
        book = get_object_or_404(Books, pk=book_id)
        bag = request.session.get('bag', {})

        bag.pop(book_id)
        messages.success(request, f'Removed {book.title} from your book bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
