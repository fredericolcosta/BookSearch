from django.urls import path

from . import views

app_name = 'library'
urlpatterns = [
    path('', views.index, name='index'),
    path('book_detail/<int:pk>/', views.DetailView.as_view(), name='book_detail'),
    path('add_book', views.AddBook.as_view(), name='add_book'),
    path('delete_book/<int:pk>/', views.DeleteBook.as_view(), name='delete_book'),
    path('update_book/<int:pk>/', views.UpdateBook.as_view(), name='update_book'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('logout', views.LogoutUser.as_view(), name='logout'),
    path('register', views.register_user, name='register'),
    path('all_categories', views.categories, name='all_categories'),
    path('add_category', views.AddCategory.as_view(), name='add_category'),
    path('delete_category/<int:pk>/', views.DeleteCategory.as_view(), name='delete_category'),
    path('update_category/<int:pk>/', views.UpdateCategory.as_view(), name='update_category'),
]