
from ..Serializers.lookupSerializer import business_category_serializer
from ..databaseModels.lookup_business_category import business_category



def get_all_business_category_details(req):
        get_business_category_data = business_category.objects.all()
        businesscategory_response = business_category_serializer(get_business_category_data, many = True).data
        return businesscategory_response
    
    

