"""View module for handling requests about orders"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from kterapi.models import Order, Vendor, Payment, Customer

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for orders"""
    class Meta:
        model = Order
        url = serializers.HyperlinkedIdentityField(
            view_name='order',
            lookup_field='id'
        )
        fields = ('id', 'url', 'vendor', 'customer', 'customer_id', 'payment', 'start', 'end', 'location')
        depth=1

class Orders(ViewSet):
    """Orders for KTER"""

    def create(self, request):
        order = Order()

        vendor = Vendor.objects.get(user=request.auth.user)
        order.vendor = vendor

        customer = Customer.objects.get(
            pk=request.data['customer_id'])
        order.customer = customer

        order.start = request.data["start"]
        order.end = request.data["end"]
        order.location = request.data["location"]
        order.save()

        serializer = OrderSerializer(order, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            order = Order.objects.get(pk=pk)
            serializer = OrderSerializer(order, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        order = Order.objects.get(pk=pk)

        vendor = Vendor.objects.get(user=request.auth.user)
        order.vendor = vendor

        payment = Payment.objects.get(
            pk=request.data['payment_id'])
        order.payment = payment

        order.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            order = Order.objects.get(pk=pk)
            order.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Order.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        orders = Order.objects.all()
        customer = self.request.query_params.get('customer_id', None)
        payment = self.request.query_params.get('payment', None)

        if customer is not None:
            orders = orders.filter(customer__id=customer)
        elif payment is not None:
            orders = orders.filter(payment__id__gte=1)

        serializer = OrderSerializer(
            orders, many=True, context={'request': request})
        return Response(serializer.data)