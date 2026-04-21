from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('items.urls')),
    path('', include('orders.urls')),
    path('success/', lambda r: HttpResponse('<h1>Payment successful!</h1>')),
]
