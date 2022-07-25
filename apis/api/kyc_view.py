import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from ..databaseService.merchant_data_service import saveGeneralInfo, savemerchantinfo
from apis.utils import Validator

@api_view(['POST'])
def save_general_info(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        name = data.get('name')
        contactNumber = data.get('contactNumber')
        emailId = data.get('emailId')
        contactDesignation = data.get('contactDesignation')
        loginMasterId = data.get('loginMasterId')
        client_code = data.get('client_code')
        
        # get_status = ""
        # if(data.get('status')):
        #     get_status =data.get('status')
        # else:
        #     get_status = MerchantStatusCode.pending.value
        
        
        request_fields = ['name', 'contactNumber', 'emailId', 'contactDesignation', 'loginMasterId', 'client_code']
       
        validation_response = Validator.validate_request_data(request_fields, data)
        if not validation_response["status"]:
            return Response(validation_response, status=status.HTTP_400_BAD_REQUEST)
        
        data_savegeneral = saveGeneralInfo(loginMasterId, client_code, name, contactNumber, emailId, contactDesignation)
                
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
    try:
        data = json.loads(request.body.decode("utf-8"))
        companyName = data.get('companyName')    
        logoPath = data.get('logoPath')
        registerdWithGST = data.get('registerdWithGST')
        gstNumber = data.get('gstNumber')
        panCard = data.get('panCard')
        signatoryPAN = data.get('signatoryPAN')
        nameOnPanCard = data.get('nameOnPanCard')
        pinCode = data.get('pinCode')
        cityId = data.get('cityId')   
        stateId = data.get('stateId')     
        registeredBusinessAdress = data.get('registeredBusinessAdress')
        operationalAddress = data.get('operationalAddress')
        loginMasterId = data.get('loginMasterId')
        client_code = data.get('client_code')
        
        # get_status = ""
        # if(data.get('status')):
        #     get_status = data.get('status')
        # else:
        #     get_status = MerchantStatusCode.pending.value
        
        request_fields = ['companyName', 'logoPath', 'registerdWithGST', 'gstNumber', 'panCard', 'signatoryPAN', 'nameOnPanCard', 'pinCode', 'cityId', 'stateId', 'registeredBusinessAdress', 'operationalAddress', 'loginMasterId', 'client_code']
        
        validation_response = Validator.validate_request_data(request_fields, data)
        if not validation_response["status"]:
            return Response(validation_response, status=status.HTTP_400_BAD_REQUEST)
        
        getdata_savemerchantinfo = savemerchantinfo(companyName, logoPath, registerdWithGST, gstNumber, panCard, signatoryPAN, nameOnPanCard, pinCode, cityId, stateId, registeredBusinessAdress, operationalAddress, loginMasterId, client_code)
        
        if getdata_savemerchantinfo:
            return Response(getdata_savemerchantinfo, status= status.HTTP_200_OK if getdata_savemerchantinfo["status"] else status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        import traceback
        message = traceback.format_exc()
        print(message)
        return Response({"message":"server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['POST'])
def save_settlement_info(request):
    pass


