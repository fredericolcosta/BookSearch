from django.db.models import fields
from rest_framework import serializers
from library.models import Book, Author, Category


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id","name"]
        extra_kwargs = {
            'name': {'validators': []},
        }

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id","name"]
        extra_kwargs = {
            'name': {'validators': []},
        }

class BookSerializer(serializers.ModelSerializer):
        
    def create(self, validated_data):
        #Check if category exists
        category = Category.objects.filter(name=validated_data['category']['name'])
        if category.count() <= 0:
            error = {'message': 'There is no such category'}
            raise serializers.ValidationError(error)

        #Check if author exists
        for author in validated_data['authors']:
            authors = Author.objects.filter(name=author['name'])
            if authors.count() <= 0:
                error = {'message': 'There is no such author'}
                raise serializers.ValidationError(error)
        
        title = validated_data['title']
        isbn = validated_data['isbn']
        pub_date = validated_data['pub_date']

        book = Book(title=title, isbn=isbn, pub_date=pub_date, category=category[0])
        book.save()
        #After creating model instance add authors
        for author in validated_data['authors']:
            author_obj = Author.objects.filter(name=author['name'])[0]
            book.authors.add(author_obj)
        

        return book
    
    def update(self, instance, validated_data):
        #Check if category exists
        category = Category.objects.filter(name=validated_data['category']['name'])
        if category.count() <= 0:
            error = {'message': 'There is no such category: ' + validated_data['category']['name']}
            raise serializers.ValidationError(error)

        #Check if author exists
        for author in validated_data['authors']:
            authors = Author.objects.filter(name=author['name'])
            if authors.count() <= 0:
                error = {'message': 'There is no such author: ' + author['name']}
                raise serializers.ValidationError(error)
            else:
                author_obj = Author.objects.filter(name=author['name'])[0]
                instance.authors.add(author_obj)

        instance.title = validated_data['title']
        instance.isbn = validated_data['isbn']
        instance.pub_date = validated_data['pub_date']
        instance.category = category[0]

        #Remove authors not in request
        old_authors  = [author['name'] for author in validated_data['authors']]
        for author in instance.authors.all():
            if author.name not in old_authors:
                if instance.authors.all().count() == 1:
                    error = {'message': 'Book has to have at least one author'}
                    raise serializers.ValidationError(error)

                instance.authors.remove(author)
        


        return instance


    authors = AuthorSerializer(many=True)
    category = CategorySerializer(many=False)

    class Meta:
        model = Book
        fields = ['id','title', 'isbn', 'pub_date', 'authors', 'category']
        

