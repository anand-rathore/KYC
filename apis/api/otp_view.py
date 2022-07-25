
from rest_framework import viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from apis.Serializers.OtpSerializer import OtpSerializer
from apis.databaseModels.otp_model import OTP
from apis.databaseService import otp_service


class OtpView(viewsets.ViewSet):
    query = OTP.objects.all()

    def create(self, request):
        serializer = OtpSerializer(data=request.data)
        if serializer.is_valid():
            otp_data = serializer.validated_data
            response = otp_service.save_otp(otp_data)
            return Response(response, status=200 if response['status'] else 400)
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def validate_otp(request):
    response = otp_service.validate_otp(request.data)
    return Response(response, status=200 if response['status'] else 400)
