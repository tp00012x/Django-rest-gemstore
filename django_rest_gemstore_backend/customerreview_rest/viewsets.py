from rest_framework import viewsets
from customerreview_rest.serializers import UploadReviewsSerializer
from reviews.models import Customer_Reviews

class UploadCustomerReviewViewSet(viewsets.ModelViewSet):
    queryset = Customer_Reviews.objects.all()
    serializer_class = UploadReviewsSerializer