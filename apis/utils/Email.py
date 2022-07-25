import threading

import requests
from apis.configuration.config import Configuration


def send_email(to_email, subject, message):
    mail_api = Configuration.get_Property("MAIL_API")
    headers = {"user-agent": "Application",
               "Accept": "*/*",
               "Content-Type": "application/json; charset=utf-8"}

    mail_data = {"toEmail": to_email,
                 "toCc": "",
                 "subject": subject,
                 "msg": message}

    response = requests.post(url=mail_api, headers=headers, json=mail_data)
    print("Email to {} sent successfully with subject {} and message {} and response {}".format(to_email, subject, message, response.text))


def email_thread(to_email, subject, message):
    thread = threading.Thread(target=send_email, args=(to_email, subject, message))
    thread.start()



