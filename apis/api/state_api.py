from rest_framework.decorators import api_view
from ..databaseService.state_service import get_lookup_state_service
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def get_all_state_details_api(req):
        try:
                get_lookup_state_data = get_lookup_state_service(req.data)
                if get_lookup_state_data:
                        return Response(get_lookup_state_data, status=status.HTTP_200_OK)

        except Exception as e:
                import traceback
                message = traceback.format_exc()
                print(message)
                return Response({"message":"server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
     
    
    

