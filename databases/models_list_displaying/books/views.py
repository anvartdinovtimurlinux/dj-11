from django.shortcuts import render, redirect
from books.models import Book
from datetime import date
from django.core.paginator import Paginator
from django.http import Http404


def get_all_dates():
        dates = [value['pub_date'] for value in Book.objects.values('pub_date')]
        dates = list(set(dates))
        dates.sort()
        return dates


def books_view(request, pub_date=None):
    template = 'books/books_list.html'
    if pub_date:
        try:
            pub_date = date.fromisoformat(pub_date)
        except ValueError:
            raise Http404
        books = Book.objects.filter(pub_date=pub_date)
        if not books:
            raise Http404
        dates = get_all_dates()
        p = Paginator(dates, 1)
        page = p.page(dates.index(pub_date) + 1)
        context = {
            'books': books,
            'paginator': page
            }
        return render(request, template, context)
    else:
        books = Book.objects.all()
    context = {
        'books': books

    }
    return render(request, template, context)


def books_view_redirect(request):
    return redirect(books_view)


def page_redirect(request, page):
    dates = get_all_dates()
    try:
        date = dates[page -1]
    except IndexError:
        raise Http404
    return redirect(books_view, pub_date=date)
