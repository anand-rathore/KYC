from apis.databaseModels.merchant_document import merchant_document
from rest_framework import serializers


class MerchantDocumentSerializer(serializers.ModelSerializer):
    files = serializers.FileField(max_length=250, allow_empty_file=False, use_url=False, write_only=True, required=True)
    client_code = serializers.CharField(max_length=50, allow_null=False, allow_blank=False, required=True, write_only=True)
    login_id = serializers.CharField(max_length=50, allow_null=False, allow_blank=False, required=True, write_only=True)

    class Meta:
        model = merchant_document
        fields = '__all__'
