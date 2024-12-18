from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Collection
from .serializers import ProductSerializer, CollectionSerializer


class ProductList(APIView):
    def get(self, request):
        queryset = Product.objects.select_related('collection').all()
        serializer = ProductSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductDetail(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if product.orderitems.count() > 0:
            return Response({"Error": "Product cannot deleted beacause it is associated with an order item."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CollectionList(APIView):
    def get(self, request):
        queryset = Collection.objects.annotate(
            products_count=Count('products')).all()
        serializer = CollectionSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CollectionDetail(APIView):
    def get(self, request, pk):
        collection = get_object_or_404(Collection.objects.annotate(
            products_count=Count('products')), pk=pk)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)

    def put(self, request, pk):
        collection = get_object_or_404(Collection.objects.annotate(
            products_count=Count('products')), pk=pk)
        serializer = CollectionSerializer(collection, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        collection = get_object_or_404(Collection.objects.annotate(
            products_count=Count('products')), pk=pk)
        if collection.products.count() > 0:
            return Response({"Error": "Collection cannot deleted beacause it is associated with a product."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
