import uuid
from django.db import models


# Create your models here.
class Customer_Reviews (models.Model):
    email = models.EmailField(max_length=254) #Stores the email
    stars = models.IntegerField() # Stores the star rating
    comments = models.TextField() #Stores the user comments