import os

from django.http import Http404, FileResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
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


@api_view(['GET'])
def get_merchant_doc(request):
    document_id = request.query_params.get('document_id')
    file_path = merchant_document_service.get_document_path_by_id(document_id)
    if file_path is None:
        raise Http404
    complete_file_path = os.getcwd() + "/" + file_path.filePath
    if os.path.exists(complete_file_path):
        response = FileResponse(open(complete_file_path, 'rb'))
        return response
    raise Http404
