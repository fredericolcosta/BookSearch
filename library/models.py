from django.db import models
from django.core.validators import RegexValidator
from django.forms import ModelForm
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

#Automatically generate token on register
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Author(models.Model):
    name = models.CharField(max_length=20, unique=True)

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


