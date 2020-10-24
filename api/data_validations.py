
from .constants import *

def validate_request(request):
    password = str(request.data['password'])
    try:
        type_of_user = request.data['type_of_user']
    except KeyError:
        type_of_user = ""
    if len(str(request.data['phone'])) != 10:
        return {'status':FAILURE,'data':INVALID_MOBILE_NUMBER},False
    elif len(str(request.data['pincode'])) != 6:
        return {'status':FAILURE,'data':INVALID_PINCODE},False
    elif len(password)< 8 or not (any(char.isupper() for char in password)) or not(any(char.islower() for char in password)):
        return {'status':FAILURE,'data':INVALID_PASSWORD},False
    elif type_of_user != USER_ADMIN and type_of_user != USER_AUTHOR and type_of_user.strip() != "":
        return {'status':FAILURE,'data':INVALID_USER_TYPE},False
    else:
        return None,True
    