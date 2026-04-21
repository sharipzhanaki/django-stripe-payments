import stripe
from stripe_payments.services import get_stripe_keys

from .models import Order


def create_payment_intent(order: Order) -> str:
    """Создаёт Stripe PaymentIntent для заказа. Возвращает client_secret."""
    _, secret_key = get_stripe_keys(order.currency)
    stripe.api_key = secret_key

    intent = stripe.PaymentIntent.create(
        amount=order.total_price,
        currency=order.currency,
        metadata={'order_id': order.pk},
    )
    return intent.client_secret
