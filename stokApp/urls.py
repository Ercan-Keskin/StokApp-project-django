from django.urls import path ,include
from rest_framework import routers

from .views import CategoryView ,BrandView ,FirmView ,ProductView, PurchasesView , SalesView

router = routers.DefaultRouter()
router.register('category', CategoryView)
router.register('brands', BrandView)
router.register('firms', FirmView)
router.register('product', ProductView)
router.register('purchases', PurchasesView)
router.register('sales', SalesView)


urlpatterns = [
    path("", include(router.urls)),
]