from django.urls import path
from .views import (
    DashBoardView,
    SalesReportView
)

urlpatterns = [
    path("dashboard", DashBoardView.as_view(), name="dashboard"),
    path(
        "sales-report/<str:start_date>/<str:end_date>/",
        SalesReportView.as_view(),
        name="sales-report"
    ),

]
