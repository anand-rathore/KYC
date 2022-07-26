from rest_framework.serializers import ModelSerializer

from apis.databaseModels.temp_kyc import TempKyc


class TempKycSerializer(ModelSerializer):
    class Meta:
        model = TempKyc
        fields = '__all__'
        read_only_fields = ('id',)
        extra_kwargs = {
            'user': {'write_only': True},
        }