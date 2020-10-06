from django.db import models
from django.core.validators import RegexValidator
from django.forms import ModelForm



class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    isbn_validator = RegexValidator(r'^[0-9]{13}|^[0-9]{10}$', 'ISBN has 10 or 13 digits.')


    title = models.CharField(max_length=50)
    isbn = models.CharField(max_length=13, unique=True,validators=[isbn_validator])
    pub_date = models.DateField('date published')    
    authors = models.ManyToManyField(Author, blank=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


