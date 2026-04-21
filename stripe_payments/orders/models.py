from django.db import models
from items.models import Item


class Discount(models.Model):
    name = models.CharField(max_length=255)
    percent_off = models.PositiveSmallIntegerField(help_text='Discount percentage, e.g. 10 = 10%')
    stripe_coupon_id = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.name} ({self.percent_off}%)'


class Tax(models.Model):
    name = models.CharField(max_length=255)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, help_text='e.g. 20.00 for 20%')
    inclusive = models.BooleanField(
        default=False,
        help_text='Inclusive: tax is included in the price. Exclusive: added on top.'
    )
    stripe_tax_rate_id = models.CharField(max_length=255, blank=True)

    def __str__(self):
        kind = 'incl.' if self.inclusive else 'excl.'
        return f'{self.name} {self.percentage}% ({kind})'


class Order(models.Model):
    items = models.ManyToManyField(Item, related_name='orders')
    discount = models.ForeignKey(Discount, null=True, blank=True, on_delete=models.SET_NULL)
    tax = models.ForeignKey(Tax, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order #{self.pk}'

    @property
    def currency(self) -> str:
        first = self.items.first()
        return first.currency if first else 'usd'

    @property
    def subtotal(self) -> int:
        return sum(item.price for item in self.items.all())

    @property
    def discount_amount(self) -> int:
        if not self.discount:
            return 0
        return round(self.subtotal * self.discount.percent_off / 100)

    @property
    def tax_amount(self) -> int:
        if not self.tax or self.tax.inclusive:
            return 0
        return round((self.subtotal - self.discount_amount) * float(self.tax.percentage) / 100)

    @property
    def total_price(self) -> int:
        return self.subtotal - self.discount_amount + self.tax_amount

    def total_price_display(self) -> str:
        return f'{self.total_price / 100:.2f}'
