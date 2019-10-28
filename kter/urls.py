from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from kterapi.models import *
from kterapi.views import *

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'user', Users, 'user')
router.register(r'vendor', Vendors, 'vendor')
router.register(r'customer', Customers, 'customer')
router.register(r'product', Products, 'product')
router.register(r'category', ProductCategories, 'productcategory')
router.register(r'order', Orders, 'order')
router.register(r'payment', Payments, 'payment')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^register$', register_user),
    url(r'^login$', login_user),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]