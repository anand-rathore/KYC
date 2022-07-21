from rest_framework import serializers
from ..databaseModels.merchant_data import merchant_data


class MerchantData(serializers.ModelSerializer):
    names = serializers.CharField(max_length=250)

    class Meta:
        model = merchant_data
        fields = ('merchantId', 'name', 'names')


class MerchantDocumentById(serializers.ModelSerializer):
    OriginialFilePath = serializers.CharField(max_length=250)

    class Meta:
        model = merchant_data
        fields = ('merchantId', 'name', 'OriginialFilePath', 'type', 'isApproved')
