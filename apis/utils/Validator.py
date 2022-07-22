def validate_request_data(fields: list, request_data):
    for key in fields:
        if not (key in request_data and request_data[key]):
            return {"status": False, "message": key + " is missing"}
    return {"status": True, "message": "Data validated successfully"}