import requests
import json

def api_login_itec(cd_usu,senha):

    url = 'http://10.10.0.56:5001/validauser'

    data = {
                "user": cd_usu,
                "pass": f"{senha}"
            }

    response = (requests.post(url, json=data)).json()

    if(response['valida'] == 'false'):
        return None
    return {'cd_usu': cd_usu}