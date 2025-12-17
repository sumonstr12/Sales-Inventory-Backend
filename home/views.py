from django.shortcuts import render
from django.db.models import Sum, Count, F
from rest_framework.response import Response
from rest_framework.views import APIView
from invoices.models import Customer, Invoice, InvoiceItem, Product
from .serializers import RecentInvoiceSerializer, SalesByCategorySerializer, TopProductSerializer
from datetime import datetime
# Create your views here.



class DashBoardView(APIView):
    permission_classes=[]
    def get(self, request):
        summary = {
            "total_revenue":Invoice.objects.aggregate(
                total=Sum("payable")
            )["total"] or 0,
            "total_orders" : Invoice.objects.count(),
            "total_customers" : Customer.objects.count(),
            
        }

        sales_by_category = (
            InvoiceItem.objects
            .values(category_name=F("product__category__name"))
            .annotate(
                sales_count=Count("id"),
                total_amount = Sum(
                    F("quantity") * F("sale_price")
                )
            )
        )

        top_products = (
            InvoiceItem.objects
            .values(
                "product_id",
                product_name=F("product__name")
            )
            .annotate(
                sold_quantity=Sum("quantity"),
                revenue=Sum(F("quantity") * F("sale_price"))
            )
            .order_by("-revenue")[:5]
        )

        recent_invoices = Invoice.objects.select_related(
            "customer"
        ).order_by("-created_at")[:5]

        return Response({
            "summary_statistics": summary,
            "sales_by_category": SalesByCategorySerializer(
                sales_by_category, many=True
            ).data,
            "top_products": TopProductSerializer(
                top_products, many=True
            ).data,
            "recent_invoices": RecentInvoiceSerializer(
                recent_invoices, many=True
            ).data
        })


class SalesReportView(APIView):
    permission_classes = []

    def get(self, request, start_date, end_date):

        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

        invoices = Invoice.objects.filter(
            created_at__date__range=(start_date, end_date)
        )

        summary = {
            "total_revenue": invoices.aggregate(
                total=Sum("payable")
            )["total"] or 0,

            "total_orders": invoices.count(),

            "total_customers": invoices.values(
                "customer_id"
            ).distinct().count(),

            "total_amount": invoices.aggregate(
                total=Sum("payable")
            )["total"] or 0,
        }

        sales_by_category = (
            InvoiceItem.objects
            .filter(invoice__in=invoices)
            .values(
                category_name=F("product__category__name")
            )
            .annotate(
                sales_count=Count("id"),
                total_amount=Sum(F("quantity") * F("sale_price"))
            )
        )

        top_products = (
            InvoiceItem.objects
            .filter(invoice__in=invoices)
            .values(
                "product_id",
                product_name=F("product__name")
            )
            .annotate(
                sold_quantity=Sum("quantity"),
                revenue=Sum(F("quantity") * F("sale_price"))
            )
            .order_by("-revenue")[:5]
        )

        recent_invoices = (
            invoices
            .select_related("customer")
            .order_by("-created_at")[:5]
            .values(
                "id",
                customer_name=F("customer__name"),
                date=F("created_at__date")
            )
        )

        return Response({
            "period": {
                "start_date": start_date,
                "end_date": end_date
            },
            "summary": summary,
            "sales_by_category": list(sales_by_category),
            "top_products": list(top_products),
            "recent_invoices": list(recent_invoices)
        })
