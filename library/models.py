from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=20)
    
class Category(models.Model):
    name = models.CharField(20, unique=True)

class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    pub_date = models.DateField('date published')    
    authors = models.ManyToManyField(Author)
    category = models.ForeignKey(Category)