from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=200)


class Product(models.Model):
    categoty = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_model = models.CharField(max_length=200)
    product_price = models.IntegerField(default=0)
