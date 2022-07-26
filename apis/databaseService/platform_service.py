from ..Serializers.lookupSerializer import platform_serializer
from ..databaseModels.lookup_platform import platform

def get_lookup_platform(req):
        get_platform_type_data = platform.objects.all()
        platofrm_type_response = platform_serializer(get_platform_type_data, many = True).data
        return platofrm_type_response
    
    