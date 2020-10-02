from django.urls import path

from . import views

app_name = 'library'
urlpatterns = [
    path('', views.index, name='index'),
    path('book_detail/<int:pk>/', views.DetailView.as_view(), name='book_detail'),
    path('add_book', views.AddBook.as_view(), name='add_book'),
    path('update_book/<int:pk>/', views.UpdateBook.as_view(), name='update_book'),
]