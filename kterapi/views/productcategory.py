"""View module for handling requests about product category"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from kterapi.models import ProductCategory

class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for product category
    Arguments:
        serializers
    """
    class Meta:
        model = ProductCategory
        url = serializers.HyperlinkedIdentityField(
            view_name='productcategory',
            lookup_field='id'
        )
        fields = ('id', 'url', 'name')

class ProductCategories(ViewSet):
    """Product categories for Bangazon"""

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized product_category instance
        """
        new_category = ProductCategory()
        new_category.name = request.data["name"]
        new_category.save()

        serializer = ProductCategorySerializer(new_category, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single category
        Returns:
            Response -- JSON serialized category instance
        """
        try:
            category = ProductCategory.objects.get(pk=pk)
            serializer = ProductCategorySerializer(category, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for an category
        Returns:
            Response -- Empty body with 204 status code
        """
        new_category = ProductCategory.objects.get(pk=pk)
        new_category.name = request.data["name"]
        new_category.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single category
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            category = ProductCategory.objects.get(pk=pk)
            category.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except ProductCategory.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to Product Category resource
        Returns:
            Response -- JSON serialized list of Product Categories
        """
        category = ProductCategory.objects.all()

        serializer = ProductCategorySerializer(
            category, many=True, context={'request': request})
        return Response(serializer.data)