from django.db import models


class Item(models.Model):
    class Currency(models.TextChoices):
        USD = 'usd', 'USD'
        EUR = 'eur', 'EUR'

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(help_text='Price in minor units (e.g. cents)')
    currency = models.CharField(max_length=3, choices=Currency.choices, default=Currency.USD)

    def __str__(self):
        return f'{self.name} ({self.price} {self.currency.upper()})'

    def price_display(self):
        """Цена в читаемом формате, например 10.99"""
        return f'{self.price / 100:.2f}'
