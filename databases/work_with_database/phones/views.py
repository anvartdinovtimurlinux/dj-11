from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone
from urllib.parse import urlencode
from django.urls import reverse


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort == 'name':
        phones = Phone.objects.order_by('name')
    elif sort == 'min_price':
        phones = Phone.objects.order_by('price')
    elif sort == 'max_price':
        phones = Phone.objects.order_by('-price')
    else:
        phones = Phone.objects.all()
    context = {
        'phones': phones,
        'sort': {
            'name': f"{reverse('catalog')}?{urlencode({'sort': 'name'})}",
            'min_price': f"{reverse('catalog')}?{urlencode({'sort': 'min_price'})}",
            'max_price': f"{reverse('catalog')}?{urlencode({'sort': 'max_price'})}",
            }.items()
        }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {'phone': phone}
    return render(request, template, context)


def home(request):
    return redirect('catalog')
