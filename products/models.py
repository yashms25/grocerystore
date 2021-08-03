from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.ImageField(upload_to='Images/')  # since url are of 2083 max characters
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in = ids)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()