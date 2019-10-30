"""View module for handling requests about vendors"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from kterapi.models import Customer, Vendor

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for customers"""
    class Meta:
        model = Customer
        url = serializers.HyperlinkedIdentityField(
            view_name='customer',
            lookup_field='id'
        )
        fields = ('id', 'url', 'vendor', 'name', 'phone', 'city')

class Customers(ViewSet):
    """Customers for KTER"""
    def create(self, request):
        customer = Customer()

        vendor = Vendor.objects.get(user=request.auth.user)
        customer.vendor = vendor
        customer.name = request.data["name"]
        customer.phone = request.data["phone"]
        customer.city = request.data["city"]
        customer.save()

        serializer = CustomerSerializer(customer, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            customer = Customer.objects.get(pk=pk)
            serializer = CustomerSerializer(customer, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        customer = Customer.objects.get(pk=pk)

        vendor = Vendor.objects.get(user=request.auth.user)
        customer.vendor = vendor
        customer.name = request.data["name"]
        customer.city = request.data["city"]
        customer.phone = request.data["phone"]
        customer.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            customer = Customer.objects.get(pk=pk)
            customer.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Customer.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        customers = Customer.objects.all()

        customer = self.request.query_params.get('vendor', None)

        current_vendor = Vendor.objects.get(user=request.auth.user)
        if customer == 'current':
            customers = customers.filter(vendor=current_vendor)

        serializer = CustomerSerializer(
            customers, many=True, context={'request': request})
        return Response(serializer.data)