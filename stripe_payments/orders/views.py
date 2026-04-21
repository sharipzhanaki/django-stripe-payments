from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from stripe_payments.services import get_stripe_keys
from .models import Order
from .services import create_payment_intent


def order_detail(request, pk: int):
    order = get_object_or_404(Order, pk=pk)
    public_key, _ = get_stripe_keys(order.currency)
    return render(request, 'orders/order_detail.html', {
        'order': order,
        'stripe_public_key': public_key,
    })


def buy_order(request, pk: int):
    order = get_object_or_404(Order, pk=pk)
    client_secret = create_payment_intent(order)
    return JsonResponse({'client_secret': client_secret})
