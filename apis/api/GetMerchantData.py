from django.http import JsonResponse
from rest_framework import status
from ..databaseModels.merchant_data import merchant_data
from ..databaseModels.merchant_document import merchant_document
from ..Serializers.merchantSerializer import MerchantData
from ..Serializers.merchantSerializer import MerchantDocumentById
from django.db.models.functions import Concat
from django.db.models import F, Value
from django.db import models
from rest_framework.views import APIView


class GetMerchantData(APIView):
    def get(self, requset):
        merchantData = merchant_data.objects.all().annotate(names=Concat(F('name'),Value('::'), F('companyName'), output_field=models.TextField()))
        serializedData = MerchantData(merchantData, many=True)
        return JsonResponse({"data": serializedData.data}, status=status.HTTP_200_OK)
        

class GetMerchantDocumentByID(APIView):
    def get(self, request):
        merchantId = request.GET['Id']
        merchantDoc = merchant_document.objects.filter(merchantId = merchantId).annotate(OriginialFilePath = Concat(Value('https://spl.sabpaisa.in'), F('filePath'), output_field=models.TextField()))
        serializedData = MerchantDocumentById(merchantDoc, many=True)
        return JsonResponse({"data": serializedData.data}, status=status.HTTP_200_OK)