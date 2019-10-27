"""View module for handling requests about payments"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from kterapi.models import Payment

class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for payments"""
    class Meta:
        model = Payment
        url = serializers.HyperlinkedIdentityField(
            view_name='payment',
            lookup_field='id'
        )
        fields = ('id', 'url', 'customer', 'merchant_name', 'account_name', 'expiration')

class Payments(ViewSet):
    """Payments for KTER"""
    def create(self, request):
        payment = Payment()

        payment.merchant_name = request.data["merchant_name"]
        payment.account_number = request.data["account_number"]
        payment.expiration = request.data["expiration"]
        payment.save()

        serializer = PaymentSerializer(payment, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            payment = Payment.objects.get(pk=pk)
            serializer = PaymentSerializer(payment, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        payment = Payment.objects.get(pk=pk)
        payment.merchant_name = request.data["merchant_name"]
        payment.account_number = request.data["account_number"]
        payment.expiration = request.data["expiration"]
        payment.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            payment = Payment.objects.get(pk=pk)
            payment.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Payment.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        payment = Payment.objects.all()

        serializer = PaymentSerializer(
            payment, many=True, context={'request': request})
        return Response(serializer.data)