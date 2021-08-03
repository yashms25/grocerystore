from django.contrib import admin
from .models import Product, Offer


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


admin.site.register(Product, ProductAdmin)
# Register your models here.
admin.site.register(Offer, OfferAdmin)
