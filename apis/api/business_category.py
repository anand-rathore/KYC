from rest_framework.decorators import api_view
from ..databaseService.business_category_service import get_all_business_category_details
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def lookup_business_category_api(req):
        try:
                get_lookup_business_category_data = get_all_business_category_details(req.data)
                if get_lookup_business_category_data:
                        return Response(get_lookup_business_category_data, status=status.HTTP_200_OK)

        except Exception as e:
                import traceback
                message = traceback.format_exc()
                print(message)
                return Response({"message":"server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
     
    
    

