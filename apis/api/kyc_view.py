import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from ..databaseService.merchant_data_service import save_general_Info, save_merchant_info
from apis.utils import Validator

# from apis.databaseService.merchant_data_service import saveGeneralInfo
from ..databaseService.merchant_data_service import save_business_info, saveSettlementInfoOther

@api_view(['PUT'])
def save_general_info_api(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        name = data.get('name')
        contact_number = data.get('contact_number')
        email_id = data.get('email_id')
        contact_designation = data.get('contact_designation')
        login_id = data.get('login_id')
        client_code = data.get('client_code')
                
        request_fields = ['name', 'contact_number', 'email_id', 'contact_designation', 'login_id', 'client_code']
       
        validation_response = Validator.validate_request_data(request_fields, data)
        if not validation_response["status"]:
            return Response(validation_response, status=status.HTTP_400_BAD_REQUEST)
        
        getdata_save_general_info = save_general_Info(login_id, client_code, name, contact_number, email_id, contact_designation)
                
        return Response(getdata_save_general_info, status= status.HTTP_200_OK if getdata_save_general_info["status"] else status.HTTP_400_BAD_REQUEST)
            
    except Exception as e:
        import traceback
        message = traceback.format_exc()
        print(message)
        return Response({"message":"server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




@api_view(['PUT'])
def save_merchant_info_api(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        company_name = data.get('company_name')    
        logo_path = data.get('logo_path')
        registerd_with_gst = data.get('registerd_with_gst')
        gst_number = data.get('gst_number')
        pan_card = data.get('pan_card')
        signatory_pan = data.get('signatory_pan')
        name_on_pancard = data.get('name_on_pancard')
        pin_code = data.get('pin_code')
        city_id = data.get('city_id')   
        state_id = data.get('state_id')     
        registered_business_address = data.get('registered_business_address')
        operational_address = data.get('operational_address')
        login_id = data.get('login_id')
        client_code = data.get('client_code')
        
        request_fields = ['company_name', 'logo_path', 'registerd_with_gst', 'gst_number', 'pan_card', 'signatory_pan', 'name_on_pancard', 'pin_code', 'city_id', 'state_id', 'registered_business_address', 'operational_address', 'login_id', 'client_code']
        
        validation_response = Validator.validate_request_data(request_fields, data)
        if not validation_response["status"]:
            return Response(validation_response, status=status.HTTP_400_BAD_REQUEST)
        
        getdata_save_merchant_info = save_merchant_info(company_name, logo_path, registerd_with_gst, gst_number, pan_card, signatory_pan, name_on_pancard, pin_code, city_id, state_id, registered_business_address, operational_address, login_id, client_code)
        
        if getdata_save_merchant_info:
            return Response(getdata_save_merchant_info, status= status.HTTP_200_OK if getdata_save_merchant_info["status"] else status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        import traceback
        message = traceback.format_exc()
        print(message)
        return Response({"message":"server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





###############################################################################################################


@api_view(['PUT'])
def save_business_info_api(request):
    try:
        request_fields = ['business_type', 'business_category', 'business_model', 'billing_label', 'company_website', 'erp_check', 'platform_id',
 'collection_type_id', 'collection_frequency_id', 'expected_transactions', 'form_build', 'ticket_size', 'client_code', 'login_id']
            
        data = json.loads(request.body.decode("utf-8"))
        validation_response = Validator.validate_request_data(request_fields, data)
        if not validation_response["status"]:
            return Response(validation_response, status=status.HTTP_400_BAD_REQUEST)
        
        business_type = data.get('business_type')
        business_category = data.get('business_category')
        business_model = data.get('business_model')
        billing_label = data.get('billing_label')
        company_website = data.get('company_website')
        erp_check = data.get('erp_check')
        platform_id = data.get('platform_id')
        collection_type_id = data.get('collection_type_id')
        collection_frequency_id = data.get('collection_frequency_id')
        expected_transactions = data.get('expected_transactions')
        form_build = data.get('form_build')
        ticket_size = data.get('ticket_size')
        client_code = data.get('client_code')
        login_id = data.get('login_id')
    
        data_business = save_business_info(business_type, business_category, business_model, billing_label, company_website, erp_check, platform_id,
        collection_type_id, collection_frequency_id, expected_transactions, form_build, ticket_size, client_code, login_id)
        if data_business:
            return Response(data_business, status=status.HTTP_200_OK)
    except Exception as e:
            return Response({"message": "server error"},status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
def save_Settlement_InfoOther(request):
    try:
        request_fields = ['account_holder_name', 'account_number','ifsc_code', 'bankId', 'account_type', 'branch', 'client_code', 'login_id']
        data = json.loads(request.body.decode("utf-8"))

        validation_response = Validator.validate_request_data(request_fields, data)
        if not validation_response["status"]:
            print("errrrrolorrrrr")
            return Response(validation_response, status=status.HTTP_400_BAD_REQUEST)
        print("A")

        account_holder_name = data.get('account_holder_name')
        account_number = data.get('account_number') 
        ifsc_code = data.get('ifsc_code')
        bankId = data.get('bankId')
        account_type = data.get('account_type')
        branch = data.get('branch')
        client_code =data.get('client_code')
        login_id =data.get('login_id')
        
        data_obj=saveSettlementInfoOther(account_holder_name, account_number, ifsc_code, bankId, account_type, branch, client_code, login_id)
                                        
        if data_obj:
            return Response(data_obj, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({"message": "server error"},status=status.HTTP_400_BAD_REQUEST)

