import traceback
from datetime import datetime
from ..databaseModels.merchant_data import merchant_data
from ..enums.merchantstatus import MerchantStatusCode


def saveGeneralInfo(loginMasterId, merchantId, businessType, yourRole, name, contactNumber, emailId,
                    contactDesignation):
    merchant_datafilter = merchant_data.objects.filter(loginMasterId=loginMasterId, merchantId=merchantId)

    if len(merchant_datafilter) > 1:
        return {"status": False, "message": "More than one records found"}

    if merchant_datafilter:
        merchant_datafilter = merchant_datafilter[0]
        merchant_datafilter.businessType = businessType
        merchant_datafilter.yourRole = yourRole

        merchant_datafilter.name = name
        merchant_datafilter.contactNumber = contactNumber
        merchant_datafilter.emailId = emailId
        merchant_datafilter.contactDesignation = contactDesignation
        merchant_datafilter.modifiedDate = datetime.now()

        merchant_datafilter.status = MerchantStatusCode.PENDING.value
        merchant_datafilter.isEmailVerified = False
        merchant_datafilter.isContactNumberVerified = False
        merchant_datafilter.save()

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

