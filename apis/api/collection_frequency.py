from rest_framework.decorators import api_view
from ..databaseService.collection_frequency_service import get_lookup_collection_frequency
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def collection_frequency_api(req):
        try:
                get_collection_frequency_data = get_lookup_collection_frequency(req.data)
                if get_collection_frequency_data:
                        return Response(get_collection_frequency_data, status=status.HTTP_200_OK)

        except Exception as e:
                import traceback
                message = traceback.format_exc()
                print(message)
                return Response({"message":"server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
     
    
    

