"""View module for handling requests about product category"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from kterapi.models import ProductCategory


class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for product categories
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
    """Product Categories for KTER"""

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized product category instance
        """
        category = ProductCategory()
        category.name = request.data["name"]
        category.save()

        serializer = ProductCategorySerializer(category, context={'request': request})

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

    def list(self, request):
        """Handle GET requests to Product Category resource
        Returns:
            Response -- JSON serialized list of Product Categories
        """
        category = ProductCategory.objects.all()

        serializer = ProductCategorySerializer(
            category, many=True, context={'request': request})
        return Response(serializer.data)