
from ..Serializers.lookupSerializer import collection_type_serializer
from ..databaseModels.lookup_collection_type import collection_type



def get_lookup_collection_type(req):
        get_collection_type_data = collection_type.objects.all()
        collectiontype_response = collection_type_serializer(get_collection_type_data, many = True).data
        return collectiontype_response
    
    

