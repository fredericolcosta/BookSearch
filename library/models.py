from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    pub_date = models.DateField('date published')    
    authors = models.ManyToManyField(Author, blank=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title