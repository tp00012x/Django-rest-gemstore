import uuid
from django.db import models


# Create your models here.
class reviews(models.Model):
    stars = models.IntegerField() # Stores the star rating
    body = models.TextField()
    author = models.TextField()