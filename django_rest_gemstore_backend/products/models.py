from django.db import models

# Create your models here.

class Products (models.Model):
    images = models.ImageField('Uploaded Gem Photo')
    description = models.TextField()
    price = models.IntegerField()
    name = models.TextField()
    canPurchase = models.BooleanField()
