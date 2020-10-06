from django.forms import models
from django.http import request
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Book, Author, Category

def index(request):
    categories = Category.objects.all()
    
    title = request.GET.get('title') 
    title = '' if title is None else title
    print(title)

    author = request.GET.get('author')
    author = '' if author is None else author
    print(author)

    category = request.GET.get('cat')

    if category != None and category != 'all':
            book_list = Book.objects.all().filter(category_id=category,authors__name__icontains=author,title__icontains=title).order_by('-title').distinct()
    else:
            book_list = Book.objects.all().filter(authors__name__icontains=author,title__icontains=title).order_by('-title').distinct()



    paginator = Paginator(book_list, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'library/index.html', {'page_obj': page_obj, "categories":categories})



class DetailView(generic.DetailView):
    model = Book
    template_name = 'library/book_detail.html'

  
class AddBook(LoginRequiredMixin, CreateView): 
  
    login_url = 'library:login'

    # specify the model for create view 
    model = Book 
  
    # specify the fields to be displayed 
    fields = '__all__'

    def get_success_url(self):
        return reverse('library:book_detail', kwargs={'pk': self.object.pk})

class UpdateBook(LoginRequiredMixin, UpdateView):

    login_url = 'library:login'

    model = Book
    fields = "__all__"
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('library:book_detail', kwargs={'pk': self.object.pk})


class LoginUser(LoginView):
    template_name="library/login.html"

class LogoutUser(LogoutView):
    next_page = "library:index"

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('library:index')
    else:
        form = UserCreationForm()
    return render(request, 'library/register.html', {'form': form})


