from ..Serializers.lookupSerializer import bank_name_serializer
from ..databaseModels.bank_master import bank_master_db



def get_bank_name_service(req):
        get_bank_name_data = bank_master_db.objects.all()
        bankname_response = bank_name_serializer(get_bank_name_data, many = True).data
        return bankname_response
    
    

