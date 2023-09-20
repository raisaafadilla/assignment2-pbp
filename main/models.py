from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    amounts = models.IntegerField()
    description = models.TextField()
    prices = models.IntegerField()
