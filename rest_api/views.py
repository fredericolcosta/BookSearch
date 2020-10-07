from django.shortcuts import render

from library.models import Book
from rest_api.serializers import Book, BookSerializer
from rest_framework import generics


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer