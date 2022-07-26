from rest_framework.decorators import api_view
from ..databaseService.business_type_service import get_all_business_type_details
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def lookup_business_type_api(req):
        try:
                get_lookup_business_type_data = get_all_business_type_details(req.data)
                if get_lookup_business_type_data:
                        return Response(get_lookup_business_type_data, status=status.HTTP_200_OK)

        except Exception as e:
                import traceback
                message = traceback.format_exc()
                print(message)
                return Response({"message":"server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
     
    
    

