from django.conf.urls import url, include
from rest_framework import routers
from customerreview_rest.viewsets import UploadCustomerReviewViewSet

router = routers.DefaultRouter()
router.register('reviews',UploadCustomerReviewViewSet,'customerreviews')

urlpatterns = [
    url(r'^', include(router.urls)) #base router
]