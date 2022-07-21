import os
from datetime import datetime

from django.core.files.storage import default_storage
from django.db import transaction

from apis.configuration.config import Configuration
from apis.databaseModels.merchant_document import merchant_document
import traceback


@transaction.atomic
def save_merchant_document(merchant_document_data):
    try:
        validation_response = validate_kyc_doc(merchant_document_data['files'])
        if not validation_response['status']:
            return validation_response
        current_path = os.getcwd()
        doc_folder = Configuration.get_Property('MERCHANT_DOC_FOLDER')
        original_file_name = merchant_document_data['files'].name
        merchant = merchant_document_data['merchant']
        merchant_doc = merchant_document()
        merchant_doc.merchant = merchant
        merchant_doc.modifiedBy = merchant_document_data['modifiedBy']
        merchant_doc.name = original_file_name
        file_path = doc_folder + "/MERCHANT_" + str(merchant.merchantId)
        file_name = generate_kyc_doc_name(merchant_document_data['files'])
        merchant_doc.filePath = file_path + "/" + file_name
        merchant_doc.type = merchant_document_data['type']
        merchant_doc.isLatest = True
        merchant_doc.createdBy = merchant_document_data['modifiedBy']
        old_document = get_document_by_merchant_id_and_type_id(merchant.merchantId, merchant_document_data['type'].id)
        if old_document.exists():
            old_document.update(isLatest=False)
        merchant_doc.save()
        complete_file_path = current_path + "/" + merchant_doc.filePath
        saved_file_name = save_file(merchant_document_data['files'], complete_file_path)
        return {"Message": "Merchant document saved successfully", "status": True}
    except Exception as e:
        traceback.print_exc()
        transaction.set_rollback(True)
        return {"Message": "Error while saving merchant document", "status": False}


def validate_kyc_doc(file):
    file_extension = file.name.split('.')[-1]
    allowed_types = Configuration.get_Property("ALLOWED_FILE_TYPES")
    if file_extension not in allowed_types:
        return {'status': False, 'message': 'File type not allowed. Allowed file types are: ' + allowed_types}
    file_size = file.size / (1024 * 1024)
    if file_size > int(Configuration.get_Property("MAX_FILE_SIZE")):
        return {'status': False, 'message': 'File size exceeds maximum limit of 3 MB'}
    return {'status': True, 'message': 'File validated successfully'}


def save_file(file, file_path):
    file_name = default_storage.save(file_path, content=file)
    return file_name


def generate_kyc_doc_name(file):
    file_extension = file.name.split('.')[-1]
    file_name = file.name.replace('.'+file_extension, '')
    file_name = file_name.replace(' ', '_') + '_' + str(datetime.now().strftime("%Y%m%d%H%M%S")) + '.' + file_extension
    return file_name


def get_document_by_merchant_id_and_type_id(merchant_id, type_id):
    merchant_doc = merchant_document.objects.filter(merchant=merchant_id, type=type_id)
    return merchant_doc
