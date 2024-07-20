from rest_framework import serializers
from .models import Product, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'mark']


class ProductListSerializer(serializers.Serializer):
    title = serializers.CharField()
    price = serializers.IntegerField()

class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price']
