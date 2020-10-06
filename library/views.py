from django.forms import models, ModelForm, DateInput
from django.http import request,response
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError
from django.contrib import messages

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

#Class form to override default date field input with HTML5 date input
class AddBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'isbn', 'pub_date', 'authors', 'category']
        widgets = {
            'pub_date': DateInput(attrs= {'type':'date'})
        }

class AddBook(LoginRequiredMixin, CreateView): 
    form_class=AddBookForm
    login_url = 'library:login'

    # specify the model for create view 
    model = Book 
  
    def get_success_url(self):
        return reverse('library:book_detail', kwargs={'pk': self.object.pk})

class DeleteBook(LoginRequiredMixin, DeleteView): 
  
    login_url = 'library:login'
    model = Book 
    success_url= reverse_lazy('library:index')#providing a reversed URL as the url attribute of a generic class-based view

class UpdateBook(LoginRequiredMixin, UpdateView):
    #Same as AddBook to re-use HTML5 date input
    form_class=AddBookForm 
    login_url = 'library:login'

    model = Book
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


def categories(request):
    categories = Category.objects.all()

    paginator = Paginator(categories, 5)

    page_number = request.GET.get('page')
    page_categories = paginator.get_page(page_number)
    return render(request, 'library/categories.html', {'page_categories': page_categories})

class AddCategory(LoginRequiredMixin, CreateView): 
    login_url = 'library:login'
    fields = '__all__'
    # specify the model for create view 
    model = Category 
  
    def get_success_url(self):
        return reverse('library:all_categories')

class DeleteCategory(LoginRequiredMixin, DeleteView): 
  
    login_url = 'library:login'
    model = Category 
    success_url= reverse_lazy('library:all_categories')#providing a reversed URL as the url attribute of a generic class-based view

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            return render(request, 'library/category_delete_error.html')

class UpdateCategory(LoginRequiredMixin, UpdateView):
    login_url = 'library:login'

    model = Category
    fields = '__all__'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('library:index')

