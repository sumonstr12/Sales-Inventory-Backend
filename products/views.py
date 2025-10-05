from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.


class ProductsCreateView(APIView):
    parser_classes = [
        MultiPartParser,
        FormParser,
    ]

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": "success",
                    "message": "Product created successfully.",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "status": "error",
                "message": "Product creation failed.",
                "data": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    

class ProductUpdateView(APIView):
    def post(self, request):
        id = request.data.get("id")
        if not id:
            return Response(
                {
                    "status": "error",
                    "message": "Product ID is required.",
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            product = Product.objects.get(id=id, category__user=request.user)
            serializer = ProductSerializer(product, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "status": "success",
                        "message": "Product updated successfully.",
                        "data": serializer.data,
                    },
                    status=status.HTTP_200_OK
                )
        except Product.DoesNotExist:
            return Response(
                {
                    "status": "error",
                    "message": "Product not found.",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(
            {
                "status": "error",
                "message": "Product update failed.",
                "data": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
class ProductDeleteView(APIView):
    def post(self, request):
        id = request.data.get("id")
        if not id:
            return Response(
                {
                    "status": "error",
                    "message": "Product ID is required.",
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            queryset = Product.objects.get(id=id)
            queryset.delete()
            return Response(
                {
                    "status": "success",
                    "message": "Product deleted successfully.",
                },
                status=status.HTTP_200_OK
            )
        except Product.DoesNotExist:
            return Response(
                {
                    "status": "error",
                    "message": "Product not found.",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
    
class ProductListIDView(APIView):
    def post(self, request):
        id = request.data.get('id')
        if not id:
            return Response(
                {
                    "status": "error",
                    "message": "Product ID is required.",
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            product  = Product.objects.get(id=id, category__user=request.user)
            serializer = ProductSerializer(product)
            return Response(
                {
                    "status": "success",
                    "message": "Product retrieved successfully.",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK
            )
        except Product.DoesNotExist:
            return Response(
                {
                    "status": "error",
                    "message": "Product not found.",
                },
                status=status.HTTP_404_NOT_FOUND
            )


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.filter(category__user=request.user)
        serializer = ProductSerializer(products, many=True)
        return Response(
            {
                "status": "success",
                "message": "Products retrieved successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK
        )