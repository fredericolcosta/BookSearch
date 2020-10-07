from rest_framework import serializers
from library.models import Book

#Defines fields automatically and implements "create()" and "update()"
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
