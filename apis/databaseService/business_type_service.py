
from ..Serializers.lookupSerializer import business_type_serializer
from ..databaseModels.lookup_business_type import business_type



def get_all_business_type_details(req):
        get_business_type_data = business_type.objects.all()
        businesstype_response = business_type_serializer(get_business_type_data, many = True).data
        return businesstype_response
    
    

