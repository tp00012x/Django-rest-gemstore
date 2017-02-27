from django.conf.urls import url,include
from rest_framework import routers
from products_rest.viewsets import ProductsViewsets

router = routers.DefaultRouter()
router.register('products',ProductsViewsets,'products')

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^', include(router.urls)) #base router
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
