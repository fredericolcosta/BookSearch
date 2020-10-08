from django.shortcuts import render

from library.models import Book, Author, Category
from rest_api.serializers import AuthorSerializer, Book, BookSerializer, CategorySerializer
from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status




class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        """
        Filters books by category or author name
        """
        book_list = Book.objects.all()
        category = self.request.query_params.get('category', None)
        author = self.request.query_params.get('author', None)
        author = '' if author is None else author

        if category != None and category != 'all':
            book_list = Book.objects.all().filter(category_id=category, authors__name__icontains=author).order_by('-title').distinct()
        else:
            book_list = Book.objects.all().filter(authors__name__icontains=author).order_by('-title').distinct()

        return book_list

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
