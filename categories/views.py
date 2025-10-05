from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer
from rest_framework import status
# Create your views here.


class CategoryListView(APIView):
    """
    View to list all categories.
    """

    def get(self, request):
        categories = Category.objects.filter(user=request.user)
        serializer = CategorySerializer(categories, many=True)
        # many=True reason hosse jate kore ekadhik category return kora jay
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class CategoryCreateView(APIView):
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
        return Response(
            {
                "status": "success",
                "message": "Category created successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED
        )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CategoryUpdateView(APIView):
    def post(self, request):
        id = request.data.get("id")
        if not id:
            return Response(
                {
                    "status": "error",
                    "message": "Category ID is required.",
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        

        try:
            if not Category.objects.filter(id=id, user=request.user).exists():
                return Response(
                    {
                        "status": "error",
                        "message": "Category not found for the user.",
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
            category = Category.objects.get(id=id, user=request.user)
            serializer = CategorySerializer(category, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "status": "success",
                        "message": "Category updated successfully.",
                        "data": serializer.data,
                    },
                    status=status.HTTP_200_OK
                )
        except Category.DoesNotExist:
            return Response(
                {
                    "status": "error",
                    "message": "Category not found.",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        


class CaterogyDeleteView(APIView):
    def post(self, request):
        id = request.data.get("id")
        if not id:
            return Response(
                {
                    "status": "error",
                    "message": "Category ID is required.",
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            if not Category.objects.filter(id=id, user=request.user).exists():
                return Response(
                    {
                        "status": "error",
                        "message": "Category not found for the user.",
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
            category = Category.objects.get(id=id, user=request.user)
            category.delete()
            return Response(
                {
                    "status": "success",
                    "message": "Category deleted successfully.",
                },
                status=status.HTTP_200_OK
            )
        except Category.DoesNotExist:
            return Response(
                {
                    "status": "error",
                    "message": "Category not found.",
                },
                status=status.HTTP_404_NOT_FOUND
            )


class CategoryListIDView(APIView):
    def post(self, request):
        id = request.data.get("id")
        if not id:
            return Response(
                {
                    "status": "error",
                    "message": "Category ID is required.",
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            category = Category.objects.get(id=id, user=request.user)
            serializer = CategorySerializer(category)
            return Response(
                {
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK
            )
        except Category.DoesNotExist:
            return Response(
                {
                    "status": "error",
                    "message": "Category not found.",
                },
                status=status.HTTP_404_NOT_FOUND
            )