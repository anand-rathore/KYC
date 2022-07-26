
from ..Serializers.lookupSerializer import state_serializer
from ..databaseModels.lookup_state import state



def get_lookup_state_service(req):
        get_lookupstate_data = state.objects.all()
        lookupstate_response = state_serializer(get_lookupstate_data, many = True).data
        return lookupstate_response
    
    

