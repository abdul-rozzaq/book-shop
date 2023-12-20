from django.shortcuts import render
from .models import Book



def home_page(request):
    queryset = Book.objects.all()
    
    context = {
        'books': queryset
    }
    return render(request, 'index.html', context)


def cart_page(request):
    context = {}
    return render(request, 'cart.html', context)


def detail_page(request, pk):
    book = Book.objects.get(pk=pk)
    
    context = {
        'book': book
    }
    
    return render(request, 'books/detail.html', context)

