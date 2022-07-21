from rest_framework import viewsets

from apis.Serializers.document_type_master_serializer import DocumentTypeMasterSerializer
from apis.databaseModels.document_type_master import DocumentTypeMaster
from apis.utils.PaginationMeta import PaginationMeta
from rest_framework.response import Response


class DocumentTypeMasterAPI(viewsets.ViewSet):
    queryset = DocumentTypeMaster.objects.all()

    def list(self, request):
        order_by = request.query_params.get('order_by', 'id')
        queryset = DocumentTypeMaster.objects.all().order_by(order_by)
        paginator = PaginationMeta()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = DocumentTypeMasterSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            serializer = DocumentTypeMasterSerializer(queryset, many=True)
            return Response(serializer.data)

