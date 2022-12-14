from django.shortcuts import render

from rest_framework import generics

from store.models import Product
from store.models import Category
from store.serializers import ProductSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
