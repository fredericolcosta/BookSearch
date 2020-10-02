from django.forms import models
from django.http import request
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse

from .models import Book, Author, Category

def index(request):
    book_list = Book.objects.all().order_by('-title')
    paginator = Paginator(book_list, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'library/index.html', {'page_obj': page_obj})



class DetailView(generic.DetailView):
    model = Book
    template_name = 'library/book_detail.html'

  
class AddBook(CreateView): 
  
    # specify the model for create view 
    model = Book 
  
    # specify the fields to be displayed 
    fields = '__all__'

    def get_success_url(self):
        return reverse('library:book_detail', kwargs={'pk': self.object.pk})

class UpdateBook(UpdateView):
    model = Book
    fields = "__all__"
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('library:book_detail', kwargs={'pk': self.object.pk})