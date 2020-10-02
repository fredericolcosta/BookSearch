from django.http import request
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Book

# Create your views here.
def index(request):
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'library/index.html', {'page_obj': page_obj})