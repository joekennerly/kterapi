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
        fields = ('id', 'url', 'company_name', 'phone', 'city', 'bio', 'user')


class Vendors(ViewSet):
    """Vendors for KTER"""
    def retrieve(self, request, pk=None):
        try:
            vendor = Vendor.objects.get(pk=pk)
            serializer = VendorSerializer(vendor, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def create(self, request):
        vendor = Vendor()
        vendor.phone = request.data["phone"]
        vendor.address = request.data["address"]
        user = Vendor.objects.get(user=request.auth.user)
        vendor.user = user

        vendor.save()
        serializer = VendorSerializer(vendor, context={'request': request})

        return Response(serializer.data)

    def list(self, request):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(
            vendors,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)