from decimal import Decimal

from rest_framework import serializers

from book.models import Author, Book


# class AuthorSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)
#     date_of_birth = serializers.DateTimeField()


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'date_of_birth']


class BookSerializer(serializers.ModelSerializer):
    # ways to secure relatioship
    # 1: nested serializing
     # author = AuthorSerializer()
    # 2: hyperlink related field
    # author = serializers.HyperlinkedRelatedField(
    #     queryset=Author.objects.all(), view_name='author-detail'
    # )

    # 3: using default, author_id

    class Meta:
        model = Book
        fields = ['title', 'author_id', 'description', 'genre', 'book_price', 'discount_price', 'language']

    # title = serializers.CharField(max_length=255)
    # author = serializers.CharField(max_length=255)
    # description = serializers.CharField(max_length=255)
    # genre = serializers.CharField(max_length=15)
    book_price = serializers.DecimalField(max_digits=6, decimal_places=2, source='price')
    discount_price = serializers.SerializerMethodField(method_name='calculate')

    def calculate(self, price):
        return price.price * Decimal(0.10)

    # language = serializers.CharField(max_length=15)
