"""View module for handling requests about vendors"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from kterapi.models import Vendor

class VendorSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for vendors"""
    class Meta:
        model = Vendor
        url = serializers.HyperlinkedIdentityField(
            view_name='vendor',
            lookup_field='id'
        )
        fields = ('id', 'url', 'company_name', 'phone', 'city', 'bio', 'user')
        depth = 1

class Vendors(ViewSet):
    """Vendors for KTER"""
    def retrieve(self, request, pk=None):
        try:
            vendor = Vendor.objects.get(pk=pk)
            serializer = VendorSerializer(vendor, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):

        vendors = Vendor.objects.filter(user=request.auth.user)

        serializer = VendorSerializer(
            vendors, many=True, context={'request': request})
        return Response(serializer.data)

    def update(self, request, pk=None):
        vendor = Vendor.objects.get(user=request.auth.user)
        vendor.user.first_name = request.data["first_name"]
        vendor.user.last_name = request.data["last_name"]
        vendor.user.email = request.data["email"]
        vendor.company_name = request.data["company_name"]
        vendor.city = request.data["city"]
        vendor.phone = request.data["phone"]
        vendor.bio = request.data["bio"]
        vendor.user.save()
        vendor.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)