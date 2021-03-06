from django.db.models.deletion import ProtectedError
from django.shortcuts import render

from library.models import Book, Author, Category
from rest_api.serializers import AuthorSerializer, Book, BookSerializer, CategorySerializer, UserSerializer
from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status, generics

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.views import APIView

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, OAuth2Authentication

from django_filters.rest_framework import DjangoFilterBackend

class BookList(generics.ListCreateAPIView):
    # Define authentication methods
    authentication_classes = [TokenAuthentication, OAuth2Authentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category','title', 'authors','isbn']

    # def get_queryset(self):
    #     """
    #     Filters books by category or author name
    #     """
    #     book_list = Book.objects.all()
    #     category = self.request.query_params.get('category', None)
    #     author = self.request.query_params.get('author', None)
    #     author = '' if author is None else author

    #     if category != None and category != 'all':
    #         book_list = Book.objects.all().filter(category_id=category,
    #                                               authors__name__icontains=author).order_by('-title').distinct()
    #     else:
    #         book_list = Book.objects.all().filter(
    #             authors__name__icontains=author).order_by('-title').distinct()

    #     return book_list


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    # Define authentication methods
    authentication_classes = [TokenAuthentication, OAuth2Authentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CategoryList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        try:
            super().destroy(self, request, *args, **kwargs)
            return Response("Deleted category", status=status.HTTP_400_BAD_REQUEST)

        except ProtectedError as e:
            return Response("Cannot delete category with books", status=status.HTTP_400_BAD_REQUEST)

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AuthorList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer