

from django.urls import path
from .views import (
    CategoryListView,
    CategoryCreateView,
    CategoryUpdateView,
    CaterogyDeleteView,
    CategoryListIDView
)

urlpatterns = [
    path("list-category", CategoryListView.as_view(), name="category-list"),
    path("create-category", CategoryCreateView.as_view(), name="category-create"),
    path("update-category", CategoryUpdateView.as_view(), name="category-update"),
    path("delete-category", CaterogyDeleteView.as_view(), name="category-delete"),
    path("category-by-id", CategoryListIDView.as_view(), name="category-by-id"),
]