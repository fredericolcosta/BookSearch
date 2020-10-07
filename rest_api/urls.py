from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>/', views.BookDetail.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('authors/', views.AuthorList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
