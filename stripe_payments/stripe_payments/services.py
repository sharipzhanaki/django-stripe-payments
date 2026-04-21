from django.conf import settings


def get_stripe_keys(currency: str) -> tuple[str, str]:
    """Возвращает пару ключей (public_key, secret_key) для указанной валюты."""
    if currency == 'eur':
        return settings.STRIPE_PUBLIC_KEY_EUR, settings.STRIPE_SECRET_KEY_EUR
    return settings.STRIPE_PUBLIC_KEY_USD, settings.STRIPE_SECRET_KEY_USD
