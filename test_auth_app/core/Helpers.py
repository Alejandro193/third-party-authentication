from json import JSONDecodeError
import requests
from django.conf import settings


def verify(headers):
    token = headers.get('HTTP_AUTHORIZATION')
    
    try:
        response = requests.post("{}users/verify/".format(settings.AUTH_SERVER_URL),
                                 data={"token": token}, headers={"uuid": settings.CLIENT_ID})
        
    except requests.exceptions.ConnectionError:
        return False
    if response.status_code in [400, 401]:
        return False
    try:
        return response.json()
    except JSONDecodeError:
        return False