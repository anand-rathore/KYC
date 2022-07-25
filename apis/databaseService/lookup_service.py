from rest_framework.decorators import api_view
from ..Serializers.lookupSerializer import lookup_state_serializer
from ..databaseModels.lookup_state import state
from rest_framework import status
from django.http import JsonResponse


@api_view(['GET'])
def get_lookup_state(req):
        get_lookupstate_data = state.objects.all()
        lookupstate_response = lookup_state_serializer(get_lookupstate_data, many = True).data
        return JsonResponse(lookupstate_response, status= status.HTTP_200_OK, safe=False)
    
    

