from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from kterapi.models import OrderProduct, Order, Product

class OrderProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderProduct
        url = serializers.HyperlinkedIdentityField(
            view_name='orderproduct',
            lookup_field='id'
        )
        fields = ('id', 'url', 'order', 'product')

class OrderProducts(ViewSet):
    def create(self, request):
        orderproduct = OrderProduct()
        order = Order.objects.get(
            pk=request.data['order_id'])
        orderproduct.order = order

        product = Product.objects.get(
            pk=request.data['product_id'])
        orderproduct.product = product

        orderproduct.save()

        serializer = OrderProductSerializer(orderproduct, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            orderproduct = OrderProduct.objects.get(pk=pk)
            serializer = OrderProductSerializer(orderproduct, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        orderproduct = OrderProduct.objects.get(pk=pk)
        order = Order.objects.get(
            pk=request.data['order_id'])
        orderproduct.order = order

        product = Product.objects.get(
            pk=request.data['product_id'])
        orderproduct.product = product
        orderproduct.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            orderproduct = OrderProduct.objects.get(pk=pk)
            orderproduct.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except OrderProduct.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        orderproducts = OrderProduct.objects.all()

        order = self.request.query_params.get('order_id', None)

        if order is not None:
            orderproducts = orderproducts.filter(order__id=order)

        serializer = OrderProductSerializer(
            orderproducts, many=True, context={'request': request})
        return Response(serializer.data)