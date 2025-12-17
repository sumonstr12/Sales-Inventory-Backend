from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import InvoiceSerializer, InvoiceItemSerializer, InvoiceDetailSerializer, InvoiceSelectSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Invoice

# Create your views here.


class InvoiceCreateView(APIView):
    permission_classes = []
    def post(self, request):
        print("raw data : " , request.data)
        serializer = InvoiceSerializer(data=request.data)
        
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(
                {
                    "status" : "success",
                    "message" : "Invoice Created Successfully",
                    "data" : serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        print(serializer.errors)
        return Response(
            {
                "status" : "failed",
                "message" : "Invoice Created Failed",
                "error" : serializer.errors
            }
        )
    
class InvoiceDeleteView(APIView):
    permission_classes = []
    def post(self, request):
        invoice_id = request.data['invoice_id']
        # print(invoice_id)
        if not invoice_id:
            return Response(
                {
                    "success" : "false",
                    "message": "Required invoice id"
                }
                ,status=status.HTTP_404_NOT_FOUND
            )
        queryset = Invoice.objects.filter(id=invoice_id).first()
        if queryset:
            queryset.delete()
            return Response(
                {
                    "success" : "True",
                    "message" : "Invoice Deleted Sucessfully"
                }, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "success" : "False",
                    "message" : "Failed to Delete ",
                }, status=status.HTTP_400_BAD_REQUEST
            )


        return Response(
            {
                "success" : "False",
                "message" : "Failed to Delete "
            }, status=status.HTTP_400_BAD_REQUEST
        )


class InvoiceDetailView(APIView):

    permission_classes = []
    def post(self, request):
        invoice_id = request.data["invoice_id"]
        # print(invoice_id)
        if not invoice_id:
            return Response(
                {
                    "status" : "False",
                    "Message" : "Required invoice id"

                }, status=status.HTTP_404_NOT_FOUND
            )
        try:
            invoice = Invoice.objects.select_related("customer").prefetch_related(
                "invoice_items__product"
            ).get(id=invoice_id)
        
            serializer = InvoiceDetailSerializer(invoice)
            return Response(
                {
                    "status" : "True",
                    "data" : serializer.data
                }
            )
        
        except Invoice.DoesNotExist:
            return Response(
                {
                    "success" : "Failed",
                    "message" : "Invoice Not Found"
                },status=status.HTTP_404_NOT_FOUND
            )

        # return Response(
        #     {
        #         "success" : "False",
        #         # "error" : serializer.error
        #     }
        # )

# This Python class defines an API view for retrieving all invoices with related customer information
# using a serializer.
class InvoiceSelectView(APIView):
    permission_classes=[]
    def get(self, request):
        invoice = Invoice.objects.select_related("customer").all()
        serializer = InvoiceSelectSerializer(invoice, many=True)
        return Response(
            {
                "success" : "True",
                "data" : serializer.data
            },status=status.HTTP_200_OK
        )