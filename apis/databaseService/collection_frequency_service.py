
from ..Serializers.lookupSerializer import collection_frequency_serializer
from ..databaseModels.lookup_collection_frequency import collection_frequency



def get_lookup_collection_frequency(req):
        get_collection_frequency_data = collection_frequency.objects.all()
        collection_frequency_response = collection_frequency_serializer(get_collection_frequency_data, many = True).data
        return collection_frequency_response
    
    

