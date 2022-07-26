import os
import traceback
from datetime import datetime

from ..configuration.config import Configuration
from ..databaseModels.merchant_data import merchant_data
from apis.databaseService import merchant_document_service


def save_general_Info(login_id, client_code, name, contact_number, email_id, contact_designation):
    get_merchant_data = merchant_data.objects.filter(loginMasterId=login_id, clientCode=client_code)

    if len(get_merchant_data) > 1:
        return {"status": False, "message": "More than one records found"}

    if get_merchant_data:
        get_merchant_data = get_merchant_data[0]
        get_merchant_data.name = name
        get_merchant_data.contactNumber = contact_number
        get_merchant_data.emailId = email_id
        get_merchant_data.contactDesignation = contact_designation
        get_merchant_data.modifiedDate = datetime.now()
        get_merchant_data.isEmailVerified = False
        get_merchant_data.isContactNumberVerified = False
        get_merchant_data.save()

        return {"status": True, "message": "Merchant data updated successfully"}
    else:
        return {"status": False, "message": "Data not found"}


def save_merchant_info(company_name, logo_path, registerd_with_gst, gst_number, pan_card, signatory_pan,
                       name_on_pancard, pin_code, city_id, state_id, registered_business_address, operational_address,
                       login_id, client_code):
    get_merchant_data = merchant_data.objects.filter(loginMasterId=login_id, clientCode=client_code)

    if len(get_merchant_data) > 1:
        return {"status": False, "message": "More than one records found"}

    if get_merchant_data:

        get_merchant_data = get_merchant_data[0]
        get_merchant_data.panCard = pan_card
        get_merchant_data.nameOnPanCard = name_on_pancard
        get_merchant_data.companyName = company_name
        get_merchant_data.registeredBusinessAdress = registered_business_address
        get_merchant_data.stateId = state_id
        get_merchant_data.pinCode = pin_code
        get_merchant_data.registerdWithGST = registerd_with_gst
        get_merchant_data.gstNumber = gst_number
        get_merchant_data.signatoryPAN = signatory_pan
        get_merchant_data.cityId = city_id
        get_merchant_data.operationalAddress = operational_address
        get_merchant_data.companyLogoPath = logo_path
        get_merchant_data.modifiedDate = datetime.now()
        get_merchant_data.save()

        return {"status": True, "message": "Merchant data updated successfully"}
    else:
        return {"status": False, "message": "Data not found"}


def get_merchant_data_by_client_code(client_code):
    try:
        merch_data = merchant_data.objects.get(clientCode=client_code)
        return merch_data
    except Exception as e:
        traceback.print_exc()
        return None


def get_merchant_data_by_client_code_and_login_id(client_code, login_id):
    try:
        merch_data = merchant_data.objects.get(clientCode=client_code, loginMasterId=login_id)
        return merch_data
    except Exception as e:
        traceback.print_exc()
        return None


def save_merchant_logo(logo, login_id, client_code):
    try:
        merchant = merchant_data.objects.get(loginMasterId=login_id, clientCode=client_code)
        current_path = os.getcwd()
        doc_folder = Configuration.get_Property('MERCHANT_DOC_FOLDER')
        file_path = doc_folder + "/MERCHANT_" + str(merchant.merchantId)
        file_name = merchant_document_service.generate_kyc_doc_name(logo)
        file_path = file_path + "/LOGO_" + file_name
        complete_file_path = current_path + "/" + file_path
        saved_file_name = merchant_document_service.save_file(logo, complete_file_path)
        return {"status": True, "file_path": file_path}
    except Exception as e:
        traceback.print_exc()
        return {"status": False, "message": "Error in saving file"}
