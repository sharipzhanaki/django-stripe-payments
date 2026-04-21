from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('order/<int:pk>/', views.order_detail, name='order_detail'),
    path('buy/order/<int:pk>/', views.buy_order, name='buy_order'),
]
