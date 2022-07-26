from apis.configuration.config import Configuration


def validate_request_data(fields: list, request_data):
    for key in fields:
        if not (key in request_data and request_data[key]):
            return {"status": False, "message": key + " is missing"}
    return {"status": True, "message": "Data validated successfully"}


def validate_file(logo):
    if not logo:
        return {"status": False, "message": "Logo is missing"}
    if logo.content_type not in ['image/jpeg', 'image/png']:
        return {"status": False, "message": "Logo must be a jpeg or png file"}
    if (logo.size / (1024 * 1024)) > int(Configuration.get_Property("MAX_FILE_SIZE")):
        return {"status": False, "message": "Logo size exceeds maximum limit of 3 MB"}
    return {"status": True, "message": "Logo validated successfully"}
