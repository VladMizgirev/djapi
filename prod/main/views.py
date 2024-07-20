from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView

from main.serializers import ProductListSerializer, ProductDetailsSerializer, ReviewSerializer
from .models import Product, Review


@api_view(['GET'])
def products_list_view(request):
    products = Product.objects.all()
    ser = ProductListSerializer(products, many=True)
    """реализуйте получение всех товаров из БД
    реализуйте сериализацию полученных данных
    отдайте отсериализованные данные в Response"""
    return Response(ser.data)


class ProductDetailsView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerializer
    """реализуйте получение товара по id, если его нет, то выдайте 404
    реализуйте сериализацию полученных данных
    отдайте отсериализованные данные в Response"""
    #return Response(ser.data)


# доп задание:
class ProductFilteredReviews(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    """обработайте значение параметра mark и
    реализуйте получение отзывов по конкретному товару с определённой оценкой
    реализуйте сериализацию полученных данных
    отдайте отсериализованные данные в Response"""
    #return Response(ser.data)
