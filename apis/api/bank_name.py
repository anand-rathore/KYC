from rest_framework.decorators import api_view
from ..databaseService.bank_name_service import get_bank_name_service
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def get_all_bank_details_api(req):
        try:
                get_bank_name_data = get_bank_name_service(req.data)
                if get_bank_name_data:
                        return Response(get_bank_name_data, status=status.HTTP_200_OK)

        except Exception as e:
                import traceback
                message = traceback.format_exc()
                print(message)
                return Response({"message":"server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
     
    
    

