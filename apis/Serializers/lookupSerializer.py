from rest_framework import serializers
from ..databaseModels.lookup_state import state
from ..databaseModels.lookup_business_type import business_type
from ..databaseModels.lookup_platform import platform
from ..databaseModels.lookup_collection_frequency import collection_frequency
from ..databaseModels.lookup_collection_type import collection_type
from ..databaseModels.bank_master import bank_master_db



class state_serializer(serializers.ModelSerializer):
    class Meta:
        model = state
        fields = '__all__'
        

class business_type_serializer(serializers.ModelSerializer):
    class Meta:
        model = business_type
        fields = '__all__'
        

class platform_serializer(serializers.ModelSerializer):
    class Meta:
        model = platform
        fields = '__all__'
        

class collection_frequency_serializer(serializers.ModelSerializer):
    class Meta:
        model = collection_frequency
        fields = '__all__'
        
class  collection_type_serializer(serializers.ModelSerializer):
    class Meta:
        model = collection_type
        fields = '__all__'
        

class bank_name_serializer(serializers.ModelSerializer):
    class Meta:
        model = bank_master_db
        fields = ('bankId', 'bankName')