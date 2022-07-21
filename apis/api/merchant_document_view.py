from rest_framework import viewsets
from rest_framework.response import Response

from apis.Serializers.merchant_document_serializer import MerchantDocumentSerializer
from apis.databaseModels.merchant_document import merchant_document
from apis.databaseService import merchant_document_service
from apis.utils.PaginationMeta import PaginationMeta


class MerchantDocumentAPI(viewsets.ViewSet):
    query = merchant_document.objects.all()

    def create(self, request):
        serializer = MerchantDocumentSerializer(data=request.data)
        if serializer.is_valid():
            merchant_document_data = serializer.validated_data
            response = merchant_document_service.save_merchant_document(merchant_document_data)
            return Response(response, status=200 if response['status'] else 400)
        return Response(serializer.errors, status=400)

    def list(self, request):
        order_by = request.query_params.get('order_by', 'documentId')
        queryset = merchant_document.objects.all().order_by(order_by)
        paginator = PaginationMeta()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = MerchantDocumentSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            serializer = MerchantDocumentSerializer(queryset, many=True)
            return Response(serializer.data)
