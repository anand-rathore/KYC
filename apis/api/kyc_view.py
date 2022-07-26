import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from ..databaseService.merchant_data_service import save_general_Info, save_merchant_info, save_merchant_logo
from apis.utils import Validator


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

        getdata_save_general_info = save_general_Info(login_id, client_code, name, contact_number, email_id,
                                                      contact_designation)

        return Response(getdata_save_general_info, status=status.HTTP_200_OK if getdata_save_general_info[
            "status"] else status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        import traceback
        message = traceback.format_exc()
        print(message)
        return Response({"message": "server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
def save_business_info(request):
    pass


@api_view(['PUT'])
def save_merchant_info_api(request):
    try:
        data = request.POST
        company_name = data.get('company_name')
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
        logo = request.FILES.get('files')

        request_fields = ['company_name', 'registerd_with_gst', 'gst_number', 'pan_card', 'signatory_pan',
                          'name_on_pancard', 'pin_code', 'city_id', 'state_id', 'registered_business_address',
                          'operational_address', 'login_id', 'client_code']

        validation_response = Validator.validate_request_data(request_fields, data)
        if not validation_response["status"]:
            return Response(validation_response, status=status.HTTP_400_BAD_REQUEST)

        validate_file = Validator.validate_file(logo)
        if not validate_file["status"]:
            return Response(validate_file, status=status.HTTP_400_BAD_REQUEST)
        save_file_response = save_merchant_logo(logo, login_id, client_code)
        if not save_file_response["status"]:
            return Response(save_file_response, status=status.HTTP_400_BAD_REQUEST)
        logo_path = save_file_response["file_path"]
        getdata_save_merchant_info = save_merchant_info(company_name, logo_path, registerd_with_gst, gst_number,
                                                        pan_card, signatory_pan, name_on_pancard, pin_code, city_id,
                                                        state_id, registered_business_address, operational_address,
                                                        login_id, client_code)

        if getdata_save_merchant_info:
            return Response(getdata_save_merchant_info, status=status.HTTP_200_OK if getdata_save_merchant_info[
                "status"] else status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        import traceback
        message = traceback.format_exc()
        print(message)
        return Response({"message": "server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
def save_settlement_info(request):
    pass
