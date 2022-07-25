import threading

import requests
from apis.configuration.config import Configuration


def send_sms(phone_number, message):
    sms_api = Configuration.get_Property("SMS_API")
    sender = "SPTRAN"
    route = "4"
    mobiles = phone_number
    message = "Dear user, " + message + " Thanks. Sabpaisa"
    authkey = "177009ASboH8XM59ce18cb"
    DLT_TE_ID = "1107161794798561616"
    country = "91"
    response = requests.post(url=sms_api, params={"sender": sender, "route": route, "mobiles": mobiles,
                                                  "authkey": authkey, "message": message, "DLT_TE_ID": DLT_TE_ID,
                                                  "country": country})

    print("Response from sms api: {}".format(response.text))


def sms_thread(phone_number, message):
    thread = threading.Thread(target=send_sms, args=(phone_number, message))
    thread.start()
