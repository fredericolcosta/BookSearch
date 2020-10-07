from django.db.models import fields
from rest_framework import serializers
from library.models import Book, Author, Category


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name"]
        extra_kwargs = {
            'name': {'validators': []},
        }

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]
        extra_kwargs = {
            'name': {'validators': []},
        }

class BookSerializer(serializers.ModelSerializer):
        
    def create(self, validated_data):
        category =Category.objects.get_or_create(name=validated_data['category']['name'])[0]
        authors = []
        

        title = validated_data['title']
        isbn = validated_data['isbn']
        pub_date = validated_data['pub_date']

        book = Book(title=title, isbn=isbn, pub_date=pub_date, category=category)
        book.save()
        for author in validated_data['authors']:
            author_obj = Author.objects.get_or_create(name=author['name'])[0]
            book.authors.add(author_obj)
        

        return book

    authors = AuthorSerializer(many=True)
    category = CategorySerializer(many=False)

    class Meta:
        model = Book
        fields = ['title', 'isbn', 'pub_date', 'authors', 'category']
        

