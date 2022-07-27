
from django.urls import path, include
from rest_framework import routers

from apis.api.GetMerchantData import GetMerchantData, GetMerchantDocumentByID
from apis.api.document_type_master_view import DocumentTypeMasterAPI
from apis.api.merchant_document_view import MerchantDocumentAPI, get_merchant_doc
from apis.api.otp_view import OtpView, validate_otp
from apis.api.kyc_view import save_general_info_api, save_merchant_info_api
from apis.api.kyc_view import save_general_info_api, save_merchant_info_api, save_business_info, save_settlement_info
from apis.api.kyc_view import save_business_info_api, save_settlement_info_other_api, save_general_info_api, save_merchant_info_api

from apis.api.state_api import get_all_state_details_api
from apis.api.business_type import lookup_business_type_api
from apis.api.platform_api import lookup_platform_type_api
from apis.api.collection_frequency import collection_frequency_api
from apis.api.collection_type import collection_type_api
from apis.api.bank_name import get_all_bank_details_api

from apis.api.kyc_view import save_general_info_api, save_merchant_info_api


router = routers.DefaultRouter()
router.register(r'document-type', DocumentTypeMasterAPI, basename='get_document_type')
router.register(r'upload-merchant-document', MerchantDocumentAPI, basename='upload_merchant_document')
router.register(r'send-otp', OtpView, basename='send_otp')

urlpatterns = [
    path('getMerchantData/', GetMerchantData.as_view()),
    path('GetMerchantDocumentByID/<int:Id>', GetMerchantDocumentByID.as_view()),
    path('get-merchant-document/', get_merchant_doc),
    path('', include(router.urls)),
    path('verify-otp/', validate_otp),
    path('save-general-info/', save_general_info_api),
    path('save-merchant-info/', save_merchant_info_api),
    path('save-business-info/',save_business_info),
    path('save-settlement-info/',save_settlement_info),


    path('get-all-state/', get_all_state_details_api),
    path('get-all-business-type/', lookup_business_type_api),
    path('get-all-platform-type/', lookup_platform_type_api),
    path('get-all-collection-frequency/',collection_frequency_api),
    path('get-all-collection-type/', collection_type_api),
    path('get-all-bank-name/',get_all_bank_details_api),
]

