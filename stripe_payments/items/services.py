import stripe
from stripe_payments.services import get_stripe_keys

from .models import Item


def create_checkout_session(item: Item, success_url: str, cancel_url: str) -> str:
    """Создаёт Stripe Checkout Session для товара. Возвращает session.id."""
    _, secret_key = get_stripe_keys(item.currency)
    stripe.api_key = secret_key

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': item.currency,
                'product_data': {
                    'name': item.name,
                    'description': item.description or None,
                },
                'unit_amount': item.price,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=success_url,
        cancel_url=cancel_url,
    )
    return session.id
