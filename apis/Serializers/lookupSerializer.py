from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from ..databaseModels.lookup_state import state
from ..databaseModels.lookup_business_type import business_type



class lookup_state_serializer(serializers.ModelSerializer):
    class Meta:
        model = state
        fields = '__all__'
        

class business_type_serializer(serializers.ModelSerializer):
    class Meta:
        model = business_type
        fields = '__all__'