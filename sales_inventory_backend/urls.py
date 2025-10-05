
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

api_urlpatterns = [
    path("",include("users.urls")),
    # path("",include("home.urls")),
    path("",include("products.urls")),
    path("",include("categories.urls")),
    path("",include("customers.urls")),
    # path("",include("invoices.urls")),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(api_urlpatterns))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)