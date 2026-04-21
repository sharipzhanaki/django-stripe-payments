from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from stripe_payments.services import get_stripe_keys
from .models import Item
from .services import create_checkout_session


def item_detail(request, pk: int):
    item = get_object_or_404(Item, pk=pk)
    public_key, _ = get_stripe_keys(item.currency)
    return render(request, 'items/item_detail.html', {
        'item': item,
        'stripe_public_key': public_key,
    })


def buy_item(request, pk: int):
    item = get_object_or_404(Item, pk=pk)
    session_id = create_checkout_session(
        item=item,
        success_url=request.build_absolute_uri('/success/'),
        cancel_url=request.build_absolute_uri(f'/item/{pk}/'),
    )
    return JsonResponse({'id': session_id})
