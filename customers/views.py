from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer
from .serializers import CustomerSerializer, CustomerListSerializer

# Create your views here.


class CustomerCreateView(APIView):
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({
                "status": "success",
                "message": "Customer created successfully.",
                "data": serializer.data,
            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "error",
            "message": "Error creating customer.",
            "errors": serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)


class CustomerUpdateView(APIView):
    def post(self, request):
        id = request.data.get("id")
        if not id:
            return Response({
                "status": "error",
                "message": "Customer ID is required.",
            }, status=status.HTTP_400_BAD_REQUEST)
        try:
            customer = Customer.objects.get(id=id, user=request.user)
            serializer = CustomerSerializer(customer, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status": "success",
                    "message": "Customer updated successfully.",
                    "data": serializer.data,
                }, status=status.HTTP_200_OK)
            return Response({
                "status": "error",
                "message": "Error updating customer.",
                "errors": serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST)
        except Customer.DoesNotExist:
            return Response({
                "status": "error",
                "message": "Customer not found for the user.",
            }, status=status.HTTP_404_NOT_FOUND)
    


class CustomerDeleteView(APIView):
    def post(self, request):
        id = request.data.get("id")
        if not id:
            return Response({
                "status": "error",
                "message": "Customer ID is required.",
            }, status=status.HTTP_400_BAD_REQUEST)
        try:
            customer = Customer.objects.get(id=id, user=request.user)
            customer.delete()
            return Response({
                "status": "success",
                "message": "Customer deleted successfully.",
            }, status=status.HTTP_200_OK)
        except Customer.DoesNotExist:
            return Response({
                "status": "error",
                "message": "Customer not found for the user.",
            }, status=status.HTTP_404_NOT_FOUND)



class CustomerListView(APIView):
    def get(self, request):
        serializer = CustomerListSerializer(
            Customer.objects.filter(user=request.user), many=True
        )

        return Response({
            "status": "success",
            "message": "Customers retrieved successfully.",
            "data": serializer.data,
        }, status=status.HTTP_200_OK)