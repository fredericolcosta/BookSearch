from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework.authtoken import views as auth_views


urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>/', views.BookDetail.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    path('authors/', views.AuthorList.as_view()),
    path('api-token/', auth_views.obtain_auth_token),
    path('register/', views.UserCreate.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
