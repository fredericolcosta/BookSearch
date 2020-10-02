from django.http import request
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views import generic

from .models import Book, Author, Category

# Create your views here.
def index(request):
    book_list = Book.objects.all().order_by('-title')
    paginator = Paginator(book_list, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'library/index.html', {'page_obj': page_obj})

class DetailView(generic.DetailView):
    model = Book
    template_name = 'library/book_detail.html'