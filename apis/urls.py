
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apis.api.GetMerchantData import GetMerchantData, GetMerchantDocumentByID
from apis.api.document_type_master_view import DocumentTypeMasterAPI
from apis.api.merchant_document_view import MerchantDocumentAPI
from apis.api.kyc_view import save_general_info


router = routers.DefaultRouter()
router.register(r'document-type', DocumentTypeMasterAPI, basename='get_document_type')
router.register(r'upload-merchant-document', MerchantDocumentAPI, basename='upload_merchant_document')

urlpatterns = [
    path('getMerchantData/', GetMerchantData.as_view()),
    path('GetMerchantDocumentByID/<int:Id>', GetMerchantDocumentByID.as_view()),
    path('', include(router.urls)),
    path('savegeneralinfo/', save_general_info),   
]

