from django.contrib import admin
from .models import Discount, Tax, Order


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'percent_off', 'stripe_coupon_id')
    readonly_fields = ('stripe_coupon_id',)


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'percentage', 'inclusive', 'stripe_tax_rate_id')
    readonly_fields = ('stripe_tax_rate_id',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'discount', 'tax', 'total_price', 'currency')
    readonly_fields = ('created_at', 'total_price', 'currency')
    filter_horizontal = ('items',)
