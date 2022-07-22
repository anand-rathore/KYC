import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from ..databaseService.merchant_data_service import saveGeneralInfo
from apis.utils import Validator

@api_view(['POST'])
def save_general_info(request):
    try:
        request_fields = ['name', 'contactNumber', 'emailId', 'contactDesignation', 'loginMasterId', 'merchantId', 'businessType', 'yourRole']
        
        data = json.loads(request.body.decode("utf-8"))
        validation_response = Validator.validate_request_data(request_fields, data)
        if not validation_response["status"]:
            return Response(validation_response, status=status.HTTP_400_BAD_REQUEST)
        name = data.get('name')
        contactNumber = data.get('contactNumber')
        emailId = data.get('emailId')
        contactDesignation = data.get('contactDesignation')
        loginMasterId = data.get('loginMasterId')
        merchantId = data.get('merchantId')
        businessType = data.get('businessType')
        yourRole = data.get('yourRole')
        
        data_savegeneral = saveGeneralInfo(loginMasterId, merchantId, businessType, yourRole, name, contactNumber, emailId, contactDesignation)
                
        return Response(data_savegeneral, status= status.HTTP_200_OK if data_savegeneral["status"] else status.HTTP_400_BAD_REQUEST)
            
    except Exception as e:
        import traceback
        message = traceback.format_exc()
        print(message)
        return Response({"message":"server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['POST'])
def save_business_info(request):
    pass


@api_view(['POST'])
def save_merchant_info(request):
    pass


@api_view(['POST'])
def save_settlement_info(request):
    pass


