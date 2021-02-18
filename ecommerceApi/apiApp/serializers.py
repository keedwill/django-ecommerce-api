from rest_framework import serializers
from .models import Category, Product, Book


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'title'
        )
        model = Category


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'title',
            'category',
            'author',
            'isbn',
            'pages',
            'stock',
            'description',
            'imgUrl',
            'status',
            'date_created'

        )
        model = Book


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'product_tag',
            'name',
            'category',
            'price',
            'stock',
            'imgUrl',
            'status',
            'date_created'

        )
        model = Product
