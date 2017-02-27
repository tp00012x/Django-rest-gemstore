from rest_framework import serializers
from reviews.models import Customer_Reviews

class UploadReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_Reviews
        fields = ('pk','email','stars','comments')