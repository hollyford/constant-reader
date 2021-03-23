from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from books.models import Books
# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, book_id):
    """ Add a quantity of the specified product to the shopping bag """

    book = Books.objects.get(pk=book_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if book_id in list(bag.keys()):
        bag[book_id] += quantity
    else:
        bag[book_id] = quantity
        messages.success(request, f'Added {book.title} to your book bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, book_id):
    """ adjust the quantity of the specified product to the specified amount """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[book_id] = quantity
    else:
        bag.pop(book_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, book_id):
    """ remove item from the shopping bag """
    try:
        bag = request.session.get('bag', {})

        bag.pop(book_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
