
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apis.api.GetMerchantData import GetMerchantData, GetMerchantDocumentByID
from apis.api.document_type_master_view import DocumentTypeMasterAPI
from apis.api.merchant_document_view import MerchantDocumentAPI, get_merchant_doc
from apis.databaseService.lookup_service import get_lookup_state
from apis.api.kyc_view import save_business_info_api, save_Settlement_InfoOther, save_general_info_api, save_merchant_info_api


router = routers.DefaultRouter()
router.register(r'document-type', DocumentTypeMasterAPI, basename='get_document_type')
router.register(r'upload-merchant-document', MerchantDocumentAPI, basename='upload_merchant_document')

urlpatterns = [
    path('getMerchantData/', GetMerchantData.as_view()),
    path('GetMerchantDocumentByID/<int:Id>', GetMerchantDocumentByID.as_viewc()),
    path('get-merchant-document/', get_merchant_doc),
    path('', include(router.urls)),
    path('savegeneralinfo/', save_general_info_api),
    path('savemerchantinfo/', save_merchant_info_api),
    path('getlookupstate/', get_lookup_state),
    path('savebusinessinfo/', save_business_info_api), 
    path('saveSettlementInfoOther/', save_Settlement_InfoOther)
]

