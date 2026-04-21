from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('buy/<int:pk>/', views.buy_item, name='buy_item'),
]
