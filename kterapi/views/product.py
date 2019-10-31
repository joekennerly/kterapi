"""View module for handling requests about products"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from kterapi.models import Product, Vendor, ProductCategory

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for product"""
    class Meta:
        model = Product
        url = serializers.HyperlinkedIdentityField(
            view_name='product',
            lookup_field='id'
        )
        fields = ('id', 'url', 'name', 'vendor', 'productcategory', 'productcategory_id', 'price', 'description')

class Products(ViewSet):
    """Products for KTER"""

    def create(self, request):
        product = Product()

        vendor = Vendor.objects.get(user=request.auth.user)
        product.vendor = vendor
        productcategory = ProductCategory.objects.get(
            pk=request.data['productcategory_id'])

        product.productcategory = productcategory
        product.name = request.data["name"]
        product.price = request.data["price"]
        product.description = request.data["description"]
        product.save()

        serializer = ProductSerializer(product, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        product = Product.objects.get(pk=pk)

        vendor = Vendor.objects.get(user=request.auth.user)
        productcategory = ProductCategory.objects.get(
            pk=request.data['productcategory_id'])

        product.vendor = vendor
        product.productcategory = productcategory
        product.name = request.data["name"]
        product.price = request.data["price"]
        product.description = request.data["description"]
        product.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
            product.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Product.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        products = Product.objects.all()
        product = self.request.query_params.get('vendor', None)

        current_vendor = Vendor.objects.get(user=request.auth.user)
        if product == 'current':
            products = products.filter(vendor=current_vendor)

        serializer = ProductSerializer(
            products, many=True, context={'request': request})
        return Response(serializer.data)