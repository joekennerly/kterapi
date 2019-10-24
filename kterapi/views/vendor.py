"""View module for handling requests about vendors"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from kterapi.models import Vendor


class VendorSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for vendors

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = Vendor
        url = serializers.HyperlinkedIdentityField(
            view_name='vendor',
            lookup_field='id'
        )
        fields = ('id', 'url', 'company_name', 'phone', 'city', 'bio', 'user_id')


class Vendors(ViewSet):
    """Vendors for KTER"""

    def list(self, request):
        """Handle GET requests to vendor resource

        Returns:
            Response -- JSON serialized list of vendors
        """
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(
            vendors,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)