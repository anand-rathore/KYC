import threading
import time

from apis.databaseModels.otp_model import OTP
from apis.utils import generator
from apis.enums.otpcodes import OtpStatus, OtpType
from apis.configuration.config import Configuration
from apis.utils import Sms, Email


def save_otp(otp):
    otp = OTP(**otp)
    otp.otp = generator.generate_otp()
    otp.status = OtpStatus.PENDING.value
    otp.verification_token = generator.generate_verification_token()
    if otp.otp_type.lower() == OtpType.PHONE.value.lower():
        otp.otp_type = OtpType.PHONE.value
        send_otp_sms(otp.mobile_number, "Your OTP for {} is {}".format(otp.otp_for, otp.otp))
    elif otp.otp_type.lower() == OtpType.EMAIL.value.lower():
        otp.otp_type = OtpType.EMAIL.value
        send_otp_email(otp.email, "Sabpaisa OTP", "Your OTP for {} is {}".format(otp.otp_for, otp.otp))
    else:
        return {'status': False, 'message': 'Invalid OTP type. Valid types are: Phone, Email'}
    otp.save()
    expire_otp_thread(otp.id)
    return {'status': True, 'verification_token': otp.verification_token}


def save_email_otp(email: str):
    otp = OTP()
    otp.otp = generator.generate_otp()
    otp.email = email
    otp.status = OtpStatus.PENDING.value
    otp.verification_token = generator.generate_verification_token()
    otp.save()
    return {'status': True, 'otp': otp.otp, 'verification_token': otp.verification_token}


def expire_otp(otp_id: int):
    otp = OTP.objects.get(id=otp_id)
    otp.is_expired = True
    otp.status = OtpStatus.EXPIRED.value
    otp.save()
    return {'status': True}


def expire_otp_thread(otp_id: int):
    otp_expire_time = Configuration.get_Property("OTP_EXPIRE_TIME")

    class expire_otp_inner_thread(threading.Thread):
        def __init__(self, otp_id):
            threading.Thread.__init__(self)
            self.otp_id = otp_id

        def run(self):
            time.sleep(60 * int(otp_expire_time))
            expire_otp(self.otp_id)

    expire_otp_inner_thread(otp_id).start()


def send_otp_sms(mobile_number: str, message: str):
    Sms.sms_thread(mobile_number, message)


def send_otp_email(to: str, subject: str, message: str):
    Email.email_thread(to, subject, message)


def validate_otp(otp_data):
    otp = otp_data.get('otp')
    verification_token = otp_data.get('verification_token')
    if not otp or not verification_token:
        return {'status': False, 'message': 'Invalid OTP data'}
    try:
        otp = OTP.objects.get(verification_token=otp_data['verification_token'], otp=otp_data['otp'])
        if otp.is_expired:
            return {'status': False, 'message': 'OTP is expired'}
        if otp.status == OtpStatus.VERIFIED.value:
            return {'status': False, 'message': 'OTP is already verified'}
        else:
            otp.status = OtpStatus.VERIFIED.value
            otp.save()
            return {'status': True, 'message': 'OTP verified successfully'}
    except OTP.DoesNotExist:
        return {'status': False, 'message': 'Invalid OTP'}
