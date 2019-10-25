from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from kterapi.models import *
from kterapi.views import Vendors, register_user, login_user, ProductCategories

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'vendor', Vendors, 'vendor')
router.register(r'productcategory', ProductCategories, 'productcategory')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^register$', register_user),
    url(r'^login$', login_user),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]